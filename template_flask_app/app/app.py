from flask import Flask
from redis import Redis
import rq
from flask_wtf.csrf import CSRFProtect
from template_flask_app.config import Config
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman

from template_flask_app.app import main_site

csrf = CSRFProtect()
limiter = Limiter(key_func=get_remote_address, default_limits=["3200/hour", "10/5second"])
talisman = Talisman(content_security_policy=False)

def setup_redis(app):
    app.redis = Redis.from_url(app.config['REDIS_URL'])
    app.task_queue = rq.Queue('tasks', connection=app.redis, default_timeout=600)
    app.redis_queues = [app.task_queue]

def setup_extensions(app, use_talisman):
    csrf.init_app(app)
    if use_talisman == True:
        talisman.init_app(app, content_security_policy=False)
    csrf.init_app(app)
    limiter.init_app(app)

def register_blueprints(app):
    app.register_blueprint(main_site.bp)


def create_app(config_class=Config, use_talisman=True):
    app = Flask(__name__)
    app.config.from_object(config_class)

    setup_extensions(app, use_talisman)
    register_blueprints(app)
    setup_redis(app)

    return app

app = create_app()