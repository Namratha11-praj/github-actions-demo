from flask import Flask, request

app = Flask(__name__)


def calculate_result(mark1, mark2, mark3):
    total = mark1 + mark2 + mark3
    average = total / 3

    if average >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    return total, average, result


@app.route("/")
def home():
    return """
    <h1>Student Result Application</h1>

    <form action="/result" method="post">
        Student Name:
        <input type="text" name="name"><br><br>

        Mark 1:
        <input type="number" name="mark1"><br><br>

        Mark 2:
        <input type="number" name="mark2"><br><br>

        Mark 3:
        <input type="number" name="mark3"><br><br>

        <input type="submit" value="Calculate Result">
    </form>
    """


@app.route("/result", methods=["POST"])
def result():
    name = request.form["name"]

    mark1 = int(request.form["mark1"])
    mark2 = int(request.form["mark2"])
    mark3 = int(request.form["mark3"])

    total, average, result = calculate_result(
        mark1, mark2, mark3
    )

    return f"""
    <h1>Student Result</h1>

    Student Name: {name}<br>
    Total: {total}<br>
    Average: {average:.2f}<br>
    Result: {result}
    """


if __name__ == "__main__":
    app.run(debug=True)