from flask import Flask, redirect, url_for, request


app = Flask(__name__)
num = 0

@app.route('/', methods = ['POST', 'GET'])
def main():
   global num
   if request.method == 'POST':
      num = request.get_json()['num']
      print(num)
      return str(num)
   else:
      print(num)
      return str(num)

if __name__ == '__main__':
   # app.run(debug = True)
   app.run(host="0.0.0.0", port=6000)