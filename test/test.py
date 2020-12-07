"""
1. read file. Send file. Call upload api
2. dimension, url call edit api
"""

from flask import Flask, render_template, request, abort, send_file
from threading import Thread
from PIL import Image
from bs4 import BeautifulSoup
import os, io
import requests
import time, json

# file paths
absolute_path = os.path.dirname(__file__)  # D:\UB CSE\ImageProcessor\
test_dir = os.path.join(absolute_path, 'test')  # D:\UB CSE\ImageProcessor\test

class UrlThread(Thread):
    def run(self) -> None:
        with open("DP.jpeg", "rb") as img:
            data = {
                'file': img
            }
            upload_response = requests.post('http://127.0.0.1:5000/image', files=data)
            soup = BeautifulSoup(upload_response.content, "html.parser")
        if upload_response:
            edit_url = soup.form.attrs['action'] + "?height=100&width=100"
            edit_response = requests.post(edit_url)
            print(edit_response)


def make_n_requests(num_requests):
    threads = []

    for i in range(num_requests):
        threads.append(UrlThread())
    start = time.time()
    # The requests will be almost simultaneous.
    # Second request will be made within nanoseconds of making the first request.

    for thread in threads:
        thread.start()  # Threads will be started without waiting for response of previous threads

    for thread in threads:
        thread.join()  # Wait for response for all the requests.
    end = time.time()
    print("Time to get response for %d simultaneous requests" % (num_requests,), end - start)


if __name__ == "__main__":
    make_n_requests(10)
