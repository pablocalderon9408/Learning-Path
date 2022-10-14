import requests
import threading
import time
from decorators import execution_time

# @execution_time
def get_name():
    response = requests.get("https://randomuser.me/api/")
    if response.status_code == 200:
        results = response.json().get("results")
        name = results[0].get("name").get("first")
        print(name)


if __name__== "__main__":
    counter = 0
    for _ in range(0, 5):
        #concurrency
        print(f"Voy en {counter}")
        thread = threading.Thread(target=get_name())
        time.sleep(1)
        thread.start()

        # # normal
        # print(f"Normal: {get_name()}")