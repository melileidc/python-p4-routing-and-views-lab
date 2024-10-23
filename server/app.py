#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return f'<h1>{param}</h1>'

@app.route('/count/<int:param>')
def count(param):
    numbers = '\n'.join(str(num) for num in range(param))
    return f'<pre>{numbers}</pre>'

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1,opertion,num2):
    result = None
    if opertion == '+':
        result = num1 + num2
    elif opertion == '-':
        result = num1 - num2
    elif opertion == '*':
        result = num1 * num2
    elif opertion == 'div':
        result = num1 / num2
    elif opertion == '%':
        result = num1 % num2
    return f'<h1>{result}</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
    
    