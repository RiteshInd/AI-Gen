# multithreading example to print current time from multiple threads

import threading
import time

class MyThread(threading.Thread):
    
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print('Starting thread %s.' % self.name)
        thread_lock.acquire()
        print_numbers(self.name, self.delay)
        thread_lock.release()

def print_numbers(threadName, delay):
    counter = 0
    while counter < 3:
        time.sleep(delay)
        print('%s: %s' % (threadName, time.ctime(time.time())))
        counter += 1

thread_lock = threading.Lock()
threads = []

# Create new threads
thread1 = MyThread("Thread-1", 1)
thread2 = MyThread("Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
    t.join()
    print('Exiting Main Thread.')


# multiprocessing example to scrape multiple URLs concurrently

# import requests
# from multiprocessing import Pool
# from bs4 import BeautifulSoup

# # Define the list of URLs to be scraped
# urls = ["https://en.wikipedia.org/wiki/Formula_One","https://en.wikipedia.org/wiki/2021_Formula_One_World_Championship",
#         "https://f1.fandom.com/wiki/Formula_1_Wiki","https://liquipedia.net/formula1/Main_Page"]


# def scrape(url):
#     """
#     Function to fetch a webpage and extract its title using BeautifulSoup
#     """
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")
#     # Assume that the page title is contained within <title> tags
#     title = soup.find("title").text
#     return title

# if __name__ == "__main__":
    
#     # Define the multiprocessing pool
#     with Pool(processes=4) as pool:
#         # Use the pool's map method to apply the scrape function to every URL
#         results = pool.map(scrape, urls)
    
#     # Print the results
#     for url, title in zip(urls, results):
#         print(f"Title of {url} is {title}")