import aiohttp
import asyncio
import json

async def func():
    async with aiohttp.ClientSession() as session:
        response = await session.get("https://cesar.airarabia.com/")
        print(response.status)
        print(response.url)
        response1 = await session.get("https://google.com/")
        print(response1.status)
        print(response1.url)

    # json_data = []
    #
    # json_data.append([response.url, response.status])
    # print(json_data)
    # with open("url_statuscode.json", "w") as jsonfile:
    #     json.dump(json_data, jsonfile)


loop = asyncio.new_event_loop()
loop.create_task(func())
loop.run_forever()
