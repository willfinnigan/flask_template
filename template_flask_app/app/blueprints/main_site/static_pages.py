from template_flask_app.app.blueprints.main_site import bp
from flask import render_template
from template_flask_app.app.blueprints.main_site.forms import AForm

@bp.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@bp.route('/a_form', methods=['GET', 'POST'])
def a_form():
    form = AForm()

    if form.validate_on_submit() == True:
        form_data = form.data
    return render_template('a_form.html', form=form)

@bp.route('/network', methods=['GET'])
def network():
    return render_template('network.html', nodes=[], edges=[], options={})