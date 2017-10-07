from flask import Flask, render_template, request
from wtforms import Form, StringField, validators
import hashlib, csv

app = Flask(__name__)

class NameForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=25)])

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template ('index.html')

@app.route('/generate/<name>', methods=['GET', 'POST'])
def generate(name):
    form = NameForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        hash_object = hashlib.md5(name.encode('utf8'))
        value = int(hash_object.hexdigest(), 16)
        if value % 2 == 0:
            return 'Desus Nice'
        else:
            return 'The Kid Mero'

    return render_template('generate.html', form=form)

if __name__ == "__main__":
    app.run()
