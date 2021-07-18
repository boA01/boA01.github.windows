# import longging; longging.basicConfig(level=longging.INFO)

from aiohttp import web

async def index(request):
    return web.Response(body=b'<h1>hello</h1>', content_type='text/html')

app = web.Application()
app.add_routes([web.get('/', index)])
web.run_app(app, host='localhost',port=9000)