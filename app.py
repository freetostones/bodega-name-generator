from flask import Flask, render_template, request
import hashlib
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template ('index.html')

@app.route('/generate/<name>')
def generate(name):
    hash_object = hashlib.md5(name.encode('utf8'))
    value = int(hash_object.hexdigest(), 16)
    if value % 2 == 0:
        return 'Desus Nice'
    else:
        return 'The Kid Mero'


if __name__ == "__main__":
    app.run()
