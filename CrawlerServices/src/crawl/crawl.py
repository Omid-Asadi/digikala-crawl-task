from requests import request

from configure.logger import process_log
from databases.postgres.postgres import product_setter, shop_setter
from configure.constants import TARGET_URL, STOP_FLAG, DETAIL_KEY, START_PAGE, BULK_LINK_BATCH_SIZE
from databases.mongo.mongo import save_link_to_mongo, get_link_from_mongo, set_crawled_flag
from lib.tools import url_builder


def crawl(is_detailed):
    try:
        if not is_detailed:
            process_log.info(f"['list-view crawling started!']")
            url_list = []
            link_extractor_manager(START_PAGE, url_list)
            process_log.info(f"['list-view crawling ended!']")

        else:
            process_log.info(f"['detail-view crawling started!']")
            detail_extractor_manager()
            process_log.info(f"['detail-view crawling ended!']")
    except Exception as e:
        process_log.error(f"[{str(e)}]")


def link_extractor_manager(page, url_list):
    process_log.info(f"['link_extractor_manager gets ready for page {page} with {BULK_LINK_BATCH_SIZE} product(s)!']")
    last_batch_link, result = link_extractor(url=url_builder(TARGET_URL, page=page), url_list=url_list)
    page = page + 1
    if result:
        if not result.acknowledged:
            process_log.error(f"['problem in storing links into mongo happened!']")

    """ Checking the final batch links, then extract sub links again. """
    return link_extractor_manager(page=page, url_list=url_list) if is_crawling(last_batch_link) else None


def link_extractor(url, url_list, method='get', count=3):
    try:
        mongo_result = None

        if count > 0:
            response = request(url=url, method=method)
            if response.status_code == 200:
                process_log.info(f"['one response has been received from a request!']")
                results = response.json()
                for each in results.get('results'):
                    url_list.append({'link': each.get(DETAIL_KEY), 'flag': False})
                try:
                    mongo_result = save_link_to_mongo(url_list) if url_list else None
                    process_log.info(f"['a new part of links has been inserted into mongo!']")

                except Exception as e:
                    process_log.error(f"[mongo faced a problem: {str(e)}]")

                url_list = []
                return results, mongo_result
            return link_extractor(url, url_list, method=method, count=count - 1)
        return False, False
    except Exception as e:
        process_log.info(f"['{str(e)}']")
        return link_extractor(url, url_list, method=method, count=count - 1) if count > 0 else None


def is_crawling(data):
    """ stop condition checker """
    try:
        return True if data.get(STOP_FLAG) else False
    except Exception as e:
        process_log.info(f"['is_crawling condition changed to False! {str(e)}']")
        return False


def detail_extractor_manager():
    process_log.info(f"['detail_extractor_manager gets ready for getting data from mongo!']")
    url_objects = get_link_from_mongo()
    detail_extractor(url_objects)


def detail_extractor(url_objects, method='get', count=3):
    try:
        if count > 0:
            for url_object in url_objects:
                export_dict_product = {}
                response = request(url=url_object.get("link"), method=method)
                if response.status_code == 200:
                    process_log.info(f"['a success response has been received for extracting data!']")

                    result = response.json()

                    """ Let's fill the Product table """

                    if result.get('structural_specs', {}).get('headers', []):
                        export_dict_product.update({

                            'brand': result.get('structural_specs', {}).get('headers', [{}])[0].get('specs', {}).get(
                                '????????', ''),

                            'capacity':
                                result.get('structural_specs', {}).get('headers', [{}])[0].get('specs', {}).get(
                                    '?????????? ??????????', ''),

                            'minimum_market_price': result.get('price'),
                        })

                        product_id = product_setter(
                            brand=export_dict_product.get("brand", ''),
                            minimum_market_price=export_dict_product.get("minimum_market_price"),
                            capacity=export_dict_product.get("minimum_market_price", '')),

                        process_log.info(f"['a new product row data has been inserted successfully!']") if product_id \
                            else None

                        """ inserting data into the shop table """
                        export_dict_shop = {}
                        shop_id = None
                        if result.get('products_info', {}).get('result'):
                            for each_shop in result.get('products_info', {}).get('result'):
                                export_dict_shop.update({
                                    'shop_name': each_shop.get('shop_name'),
                                    'price': each_shop.get('price')
                                })
                        if product_id and isinstance(product_id, tuple):
                            shop_id = shop_setter(
                                name=export_dict_shop.get('shop_name'),
                                price=export_dict_shop.get('price'),
                                product=product_id[0]
                            )
                            process_log.info(
                                f"['some new shop row(s) data has been inserted successfully!']") if shop_id else None

                        if shop_id and product_id:
                            set_crawled_flag(link_id=url_object.get('_id'))
                            process_log.info(
                                f"['a link for product ID {product_id} has been turned to crawled in mongoDB']")

    except Exception as e:
        process_log.info(f"['{str(e)}']")
        return detail_extractor(url_objects, method=method, count=count - 1) if count > 0 else None
