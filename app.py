import flask
from flask import Flask, render_template, request, redirect, url_for
from utils.Permutations import permute

app = Flask(__name__)
history = []


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def main_post():
    text = request.form['text']
    history.append(text)
    data = list(text)
    permuted_text = []
    permute(data, permuted_text)
    return render_template('show_permutations.html', data=permuted_text, history=history)


if __name__ == '__main__':
    app.run()
