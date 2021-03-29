from flask import Flask, render_template , redirect , url_for , request

app = Flask(__name__)

@app.route("/")
def top():
    return render_template("index.html")

#? 円の面積計算=================================================================
@app.route("/calcarea_form")
def calcarea_form():
    reuslt = request.args.get("result")
    return render_template("calcarea_form.html", result=reuslt)

@app.route("/calc_result")
def calc_result():
    radius = request.args.get("radius")
    if radius == None or radius == "":
        return redirect(url_for("calcarea_form", result="error"))
    result = int(radius) * int(radius) * 3.14
    return redirect(url_for("calcarea_form", result=result))
#? ｺｺﾏﾃﾞ=======================================================================

if __name__ == "__main__":
    app.run(debug=True)