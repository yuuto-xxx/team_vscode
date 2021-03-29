from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def top():
    return render_template("index.html")

@app.route("/salary")
def salary():
    return render_template("salary.html")

@app.route("/salary_result")
def salary_result():
    salary = request.args.get("salary")
    time = request.args.get("time")

    salary = int(salary) * int(time)

    return render_template("salary_result.html", salary=salary)

if __name__ == "__main__":
    app.run(debug=True)