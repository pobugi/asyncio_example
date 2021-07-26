import requests
import time

start_time = time.time()

def get_page_data(category, page_id):
    if page_id:
        url = "https://ozon.ru/brand/{}/?page={}".format(category, page_id)
    else:
        url = "https://ozon.ru/brand/{}".format(category)

    print("get url: {}".format(url))
    response = requests.get(url)
    return response.text

def load_site_data():
    categories = [
        "playstation-79966341",
        "adidas-144082850",
        "bosch-7577796",
        "lego-19159896"
    ]
    for category in categories:
        for page_id in range(100):
            text = get_page_data(category, page_id)

if __name__ == "__main__":
    load_site_data()
    execution_time = time.time() - start_time
    print("Execution time: {} s".format(int(execution_time)))