"""
#1
from aiohttp import web


async def handle(request):
    name = request.match_info.get('name', 'Anonymous')
    text = 'hello, ' + name
    return web.Response(body=text.encode('utf-8'))

app = web.Application()
app.router.add_route('GET', '/{name}', handle)

web.run_app(app)

#2
https://docs.aiohttp.org/en/stable/
"""

from aiohttp import web


async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

if __name__ == '__main__':
    web.run_app(app)
