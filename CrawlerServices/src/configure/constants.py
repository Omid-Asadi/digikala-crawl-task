START_PAGE = -1
BULK_LINK_BATCH_SIZE = 3
RUNNER = True
# TARGET_URL = "https://api.torob.com/v4/base-product/search/?category=243&sort=popularity&page={}&size={}&source=next_desktop&android_app_ver=None&_bt__experiment=&suid=63961e5ab5a0ded987cb93a8"
TARGET_URL = "https://api.torob.com/v4/base-product/search/?sort=popularity&category=243&page={}&size={}&source=next_desktop&android_app_ver=None&_bt__experiment=&suid=639cc5ff51bf64a4814eea8c"
STOP_FLAG = 'next'
DETAIL_KEY = "more_info_url"
SLEEP_TIME = 1
SLEEP_TIME_GET_LINKS_FROM_MONGO = 10
