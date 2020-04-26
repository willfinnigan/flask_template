from flask import Blueprint

bp = Blueprint('main_site', __name__, template_folder='templates')

from template_flask_app.app.blueprints.main_site import static_pages