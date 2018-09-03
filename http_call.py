import requests

url = 'https://webhook.site/1b92078a-9b76-4c7e-92cb-62a2302c8fb9'
num_calls = 3

def submit_request_and_get_headers():
    r = requests.get(url)
    print(r.headers['date'])
    return

def main():
    for i in range(num_calls):
        submit_request_and_get_headers()
if __name__ == '__main__':
    main()