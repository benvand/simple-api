from flask import render_template, flash, request
from forms import OurForm
from app import app


@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.form)
    print(request.data)
    form = OurForm()
    if request.method != "POST":
        flash('No post')
    elif form.validate_on_submit():
        flash('Good ' + str(form.data))
    else:
        flash('Bad' + str(form.data))

    return render_template('index.j2', form=form)

