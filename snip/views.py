from flask import render_template, redirect, request
from werkzeug import exceptions

from . import app
from .forms import SnipForm
from . import snipper


@app.route('/', methods=['POST', 'GET'])
def index():
    print(request.method)

    if request.method == 'GET':
        form = SnipForm()
        return render_template('index.html', form=form)

    elif request.method == 'POST':
        form = SnipForm()
        if form.validate_on_submit():
            snip = snipper.snip(form.url.data, reusable=False)
            return render_template('success.html', snip=snip)
        else:
            return render_template('index.html', form=form)
    else:
        raise exceptions.MethodNotAllowed

@app.route('/<snip>')
def snip_to(snip):
    url = snipper.unsnip(snip)
    return redirect(url)
