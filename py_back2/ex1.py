from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/info", methods=['get'])
def info_input():
   return render_template("info.html")

@app.route("/info_result", methods=['post'])
def info_result():
    name = request.form['name']
    city = request.form['city']
    return render_template('info_result.html', name=name, city=city)


app.run(debug = True)