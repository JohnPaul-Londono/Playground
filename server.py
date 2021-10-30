from flask import Flask, render_template

app = Flask(__name__)

@app.route("/play")
def three_boxes():
    return render_template("index.html",num = 3, color = "blue")

@app.route("/play/<int:num>")
def seven_boxes(num):
    return render_template("index.html", num = num, color = "blue")

@app.route("/play/<string:color>/<int:num>")
def green_boxes(color, num):
    return render_template("index.html", color = color, num = num)




if __name__=="__main__":
    app.run(debug=True)    