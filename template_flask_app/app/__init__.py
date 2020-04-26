from flask import Flask
from redis import Redis
import rq
from flask_wtf.csrf import CSRFProtect
from template_flask_app.config import Config

from template_flask_app.app.blueprints import main_site

csrf = CSRFProtect()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    csrf.init_app(app)

    app.register_blueprint(main_site.bp)

    app.redis = Redis.from_url(app.config['REDIS_URL'])
    app.task_queue = rq.Queue('tasks', connection=app.redis, default_timeout=600)

    return app




app = create_app()





