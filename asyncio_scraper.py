import asyncio
import aiohttp
import time


start_time = time.time()
# all_data = []

async def get_page_data(session, category, page_id):
    if page_id:
        url = "https://ozon.ru/brand/{}/?page={}".format(category, page_id)
    else:
        url = "https://ozon.ru/brand/{}".format(category)

    async with session.get(url) as resp:
        assert resp.status == 200
        print("get url: {}".format(url))
        response = await resp.text()
        # all_data.append(response)
        return response

async def load_site_data():
    categories = [
        "playstation-79966341",
        "adidas-144082850",
        "bosch-7577796",
        "lego-19159896"
    ]
    async with aiohttp.ClientSession() as session:
        tasks = []
        for category in categories:
            for page_id in range(100):
                task = asyncio.create_task(get_page_data(
                    session, category, page_id
                ))
                tasks.append(task)
        await asyncio.gather(*tasks)

asyncio.run(load_site_data())

execution_time = time.time() - start_time
print("Execution time: {} s".format(int(execution_time)))