from flask import Flask
app=Flask(__name__)
@app.route("/")
def home():
    return "HELLOWORLD! this is my first app on render"
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
