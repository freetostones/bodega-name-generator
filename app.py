from flask import Flask, render_template, request, jsonify
# from wtforms import Form, StringField, validators
import hashlib
import csv
import random
import pandas

app = Flask(__name__)

# HELPER FUNCTIONS
def hash(name):
    hash_object = hashlib.md5(name.encode('utf8'))
    return int(hash_object.hexdigest(), 16)

# Get a unique index from a list
def unique(value, array):
    return array[value % len(array)]

# Get a random index from a list
def arbitrary(array):
    return random.choice(array)

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/data')
def data():
    with open('nameParts.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print (arbitrary(row))

    return "Check terminal!"

@app.route('/generate', methods=['POST'])
def generate():
    name = request.form['name']
    colnames = ['pre', 'des', 'main', 'loc', 'nat']
    data = pandas.read_csv('nameParts.csv', names=colnames)
    prefix = data['pre'].dropna().values.tolist()
    descriptor = data['des'].dropna().values.tolist()
    main = data['main'].dropna().values.tolist()
    location = data['loc'].dropna().values.tolist()
    nationality = data['nat'].dropna().values.tolist()
    print (prefix)

    if name:
        value = hash(name)
        if value % 2 == 0:
            alias = unique(value, main) + ' ' + unique(value, descriptor)
            return jsonify({'name' : alias})
        else:
            alias = unique(value, prefix) + ' ' + unique(value, descriptor) + ' ' + unique(value, main)
            return jsonify({'name' : alias})

    return jsonify({'error' : 'Missing your name!'})

if __name__ == "__main__":
    app.run(debug=True)
