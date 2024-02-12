from aiohttp import web


async def handler(request):
    return web.Response(text="Hello, world")

if __name__ == '__main__':
    app = web.Application()
    app.router.add_get("/", handler=handler)
    web.run_app(app)

