from sanic import Sanic
from sanic.response import text,redirect

app = Sanic("My hello, world app")

# @app.get('/')
# async def hello_world(request):
#     return text("hello world")

@app.route("/")
async def index(request):
    url = app.url_for("post_handler", post_id=5)
    return redirect(url)

@app.route("/posts/<post_id>")
async def post_handler(request, post_id):
    return text(post_id)