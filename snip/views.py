from flask import render_template, redirect, url_for

from . import app
from .forms import SnipForm
from . import snipper


@app.route('/')
def index():
    form = SnipForm()
    return render_template('index.html', form=form)

@app.route('/snip', methods=['POST'])
def submit_snip():
    form = SnipForm()
    if form.validate_on_submit():
        snip = snipper.snip(form.url.data, reusable=False)
        return render_template('success.html', snip=snip)
    return render_template('index.html', form=form)


@app.route('/<snip>')
def snip_to(snip):
    url = snipper.unsnip(snip)
    return redirect(url)
