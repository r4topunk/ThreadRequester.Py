import requests
from concurrent.futures import ThreadPoolExecutor, as_completed


def doRequest(url):
    http_r = requests.get('http://' + url, timeout=10)
    https_r = requests.get('https://' + url)
    return http_r, https_r


urls = [
    'google.com',
    'twitter.com',
    'youtube.com',
    'facebook.com',
    'instagram.com'
]

with ThreadPoolExecutor() as executor:
    futures = []
    for url in urls:
        futures.append(executor.submit(doRequest, url))

    for task in as_completed(futures):
        #print(len(task.result()))
        for response in task.result():
            if len(response.history) == 0:
                print(f"[{response.status_code}][{response.request.url}]")
            else:
                first_response = response.history[0]
                print(f"[{first_response.status_code}][{first_response.request.url}]")
