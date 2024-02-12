import asyncio
import aiohttp

URL = "https://www.wikipedia.org/"


async def fetch(session: aiohttp.ClientSession, url: str):
    async with session.get(url) as resp:
        if resp.ok:
            return await resp.text()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, URL)
        return html


if __name__ == '__main__':
    res = asyncio.run(main())
    print(res)