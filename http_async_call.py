import requests
import threading
url = 'https://webhook.site/1b92078a-9b76-4c7e-92cb-62a2302c8fb9'
num_calls = 3

def submit_request_and_get_headers():
    r = requests.get(url)
    print(r.headers['date'])
    return

def main():
    threads = []
    for i in range(num_calls):
        threads.append(threading.Thread(target=submit_request_and_get_headers))
    
    for t in threads:
        t.start()

    for t in threads:
        t.join()
if __name__ == '__main__':
    main()