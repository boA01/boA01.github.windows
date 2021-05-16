from sanic import Sanic

app = Sanic("MyApp")

# app.db = Database()
# app.ctx.db = Database()

app.config.DB_NAME = 'appdb'
app.config['DB_USER'] = 'appuser'

db_settings = {
    'DB_HOST':'localhost',
    'DB_NAME':'appdb',
    'DB_USER':'appuser'
}
app.configx.update(db_settings)