import os
from configure.constants import RUNNER
from configure.logger import process_log
from crawl.crawl import crawl


if RUNNER:
    process_log.info(f"['crawling started!']")
    crawl(is_detailed=os.environ.get('IS_DETAILED'))
    process_log.info(f"['crawling ended successfully!']")
