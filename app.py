from flask import Flask, render_template, request, jsonify
# from wtforms import Form, StringField, validators
import hashlib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    name = request.form['name']

    if name:
        hash_object = hashlib.md5(name.encode('utf8'))
        value = int(hash_object.hexdigest(), 16)
        if value % 2 == 0:
            return jsonify({'name' : 'Desus Nice'})
        else:
            return jsonify({'name' : 'The Kid Mero'})

    return jsonify({'error' : 'Missing your name!'})

if __name__ == "__main__":
    app.run(debug=True)
