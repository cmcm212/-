# redirect : 새로운 주소로 이동 / post. 처리하고 새로운 주소로 이동
# render_template : html을 출력

from flask import Flask, redirect, render_template, request
app = Flask(__name__)

# 전역 변수 : 모든 함수가 접근가능한 공유 데이터
todos = []
tno = 1

# 내용을 출력하는 페이지
@app.route("/list")
def list():
    return render_template("list.html", todos=todos)

@app.route("/write")
def write_input():
    return render_template("write.html")

@app.route("/write", methods=['post'])
def do_write():
    global tno
    title = request.form.get("title", type=str)
    todo = {"tno":tno, "title":title, "finish":False}
    todos.append(todo)
    tno=tno+1
    return redirect("/list")

@app.route("/delete", methods=['post'])
def delete():
    tno = request.form.get('tno', type=int)
    for todo in todos:
        if todo['tno']==tno:
            todos.remove(todo)
            break
    return redirect("/list")


app.run(debug=True)