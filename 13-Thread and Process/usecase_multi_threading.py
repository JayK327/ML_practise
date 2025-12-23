#Web scraping : Using multi-threading to scrape multiple web pages concurrently to speed up data collection.
# Involves making numerous network request to fetch web page .
# These task are I/O bound because they spend most of their time waiting for server response.
# Multi-threading can help to initiate multiple request simultaneously,thereby reducing overall time taken to scrape data.

'''
https://python.langchain.com/v0.2/docs/introduction/
https://python.langchain.com/v0.2/docs/concept/
https://python.langchain.com/v0.2/docs/tutorials/
'''

import threading
import requests
from bs4 import BeautifulSoup
import time

urls=['https://python.langchain.com/v0.2/docs/introduction/',
'https://python.langchain.com/v0.2/docs/concept/',
'https://python.langchain.com/v0.2/docs/tutorials/']

def fetch_url(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    print(f'length of page at {url}:{len(soup.text)} characters')

threads=[]

start_time=time.time()

for url in urls:
    thread=threading.Thread(target=fetch_url,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()  # To ensure the main program waits for all threads to finish before continuing.

end_time=time.time()
print('Scraping completed.')
print(f'Time taken to scrape all pages: {end_time-start_time} seconds')

print("--------------------------------------------------------------")
print("\nNow performing sequential requests(Without thread):\n")
start_time = time.time()

# Perform requests sequentially
for url in urls:
    fetch_url(url)

end_time = time.time()
print(f'Time taken to scrape all pages without threading: {end_time-start_time} seconds')
