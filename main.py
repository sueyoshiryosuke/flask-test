from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  name = "名前"
  age = 20
  return render_template('index.html',
    name=name,
    age=age)
#  return "<img src=\"static/yuzu2.jpg\">"

app.run(host='0.0.0.0')