from configure.constants import BULK_LINK_BATCH_SIZE


def url_builder(base_url, page):
    return base_url.format(page, BULK_LINK_BATCH_SIZE)
