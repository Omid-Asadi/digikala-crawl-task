import os


START_PAGE = os.environ.get('START_PAGE')
BULK_LINK_BATCH_SIZE = os.environ.get('BULK_LINK_BATCH_SIZE')

TARGET_URL = "https://api.torob.com/v4/base-product/search/?category=243&sort=popularity&page={}&size={}&source=next_" \
             "desktop&android_app_ver=None&_bt__experiment=&suid=63961e5ab5a0ded987cb93a8"
STOP_FLAG = 'next'
DETAIL_KEY = "more_info_url"
