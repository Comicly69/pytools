import requests
import string
import random
import threading

def send_post_request(url, data):
    print("Sending POST request with data:", data)
    response = requests.post(url, data=data)
    status_code = response.status_code
    if status_code == 200:
        print("\033[32mStatus code:", status_code, "\033[0m")
    elif status_code == 500:
        print("\033[33mStatus code:", status_code, "\033[0m")
    else:
        print("\033[31mStatus code:", status_code, "\033[0m")

while True:
    url = input("Enter the URL to send the POST requests to: ")

    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url

    use_random_data = input("Do you want to use random data? (y/n) ")

    if use_random_data.lower() == 'y':
        num_characters = int(input("Enter the number of characters to generate: "))
        data = ''.join(random.choices(string.ascii_letters + string.digits, k=num_characters))
    else:
        data = input("Enter the data to send in the POST requests: ")

    num_threads = int(input("Enter the number of threads to use: "))

    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=send_post_request, args=(url, data))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    repeat = input("Do you want to run the program again? (y/n) ")
    if repeat.lower() != 'y':
        break
