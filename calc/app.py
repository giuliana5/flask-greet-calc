# Put your app in here.
from operations import add, sub, mult, div
from flask import Flask, request

app = Flask(__name__)

operators = {
  "add": add,
  "sub": sub,
  "mult": mult,
  "div": div
}

@app.route("/add")
def add_nums():
  """Add a and b params"""

  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  total = add(a, b)

  return str(total)

@app.route("/sub")
def sub_nums():
  """Subtract a and b params"""

  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  total = sub(a, b)

  return str(total)

@app.route("/mult")
def mult_nums():
  """Multiply a and b params"""

  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  total = mult(a, b)

  return str(total)

@app.route("/div")
def div_nums():
  """Divide a and b params"""

  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  total = div(a, b)

  return str(total)

@app.route("/math/<operation>")
def add_nums(operation):
  """Add a and b params"""

  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  total = operators[operation](a, b)

  return str(total)
