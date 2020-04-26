from template_flask_app.app.blueprints.main_site import bp
from flask import render_template


@bp.route('/', methods=['GET'])
def home():
    return render_template('home.html')