from flask import Flask,render_template


app = Flask(__name__)


@app.route("/demo", methods=['POST','GET'])
def demo():
    data=[{'a':1,'b':2,'c':3},{'a':4,'b':5,'c':6}]
    return render_template('demo.html',data=data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9875)
