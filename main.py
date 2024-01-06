import threading 
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = 'w3school'
HOMEPAGE = 'https://www.w3schools.com/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

def create_workers():
  for _ in range(NUMBER_OF_THREADS):
    t = threading.Thread(target=work)
    t.daemon = True
    t.start()

def work():
  while True:
    url = queue.get()
    Spider.crawl_page(threading.current_thread().name, url)
    queue.task_done


def create_job():
  for link in file_to_set(QUEUE_FILE):
    queue.put(link)
  queue.join()
  crawl()

def crawl():
  queued_link = file_to_set(QUEUE_FILE)
  if len(queued_link)> 0 :
    print (str(len(queued_link)) + "links in the queue")
    create_job()