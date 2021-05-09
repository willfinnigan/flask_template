import sys
from rq import Connection, Worker
import os

from template_flask_app.app.app import create_app

production_mode = os.environ.get('PRODUCTION') or False

if __name__ == '__main__':
    app = create_app(use_talisman=production_mode)
    app.app_context().push()

    with Connection(app.redis):
        qs = sys.argv[1:] or app.redis_queues
        w = Worker(qs, log_job_description=False)
