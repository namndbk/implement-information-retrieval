from flask import Flask, render_template, redirect, url_for, request
from entity import Candidate

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
@app.route('/results', methods=["GET", 'POST'])
def index():
    number = 1
    candidate = Candidate.Instance()
    if request.method == "GET":
        return render_template("index.html", arrayForm=candidate.arrayForm, number=number)
    else:
        results, flag = candidate.search(request.form)
        if flag is False:
            number = 0
        print(results)
        return render_template('index.html', results=results, number=number, arrayForm=candidate.arrayForm)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5005, debug=True)