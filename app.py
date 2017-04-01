from flask import Flask, json
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def install():
    return "installed"


if __name__ == "__main__":
    app.run(debug=True)