from flask import Flask
app = Flask(__name__)
#/hello로 접속하면 Hello world리턴
@app.route("/hello")
def hello():
    return "<h1>Hello World!</h1>"
host_addr = "0.0.0.0"
port_num = "8080"
#모듈이 아니라면 웹 서버로 띄움
if __name__ == "__main__":
    app.run(host=host_addr, port=port_num, debug=True)