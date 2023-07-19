from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [{
  'id': 1,
  'title': "python developer",
  'salary': "120k",
}, {
  'id': 2,
  'title': "web desinger",
  'salary': "100k",
}, {
  'id': 3,
  'title': "project manager",
  'salary': "80k",
}]


@app.route("/")
def main():
  return render_template("index.html", jobs=JOBS)


@app.route("/api/jobs")
def jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
