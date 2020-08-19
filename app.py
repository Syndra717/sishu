from flask import Flask, render_template
import sqlite3
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/index')
def home():
    return index()


@app.route('/rank')
def rank():
    datalist = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template("rank.html", movies=datalist)


@app.route('/score')
def score():
    score = []
    num = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select score,count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        score.append(item[0])
        num.append(item[1])
    cur.close()
    con.close()
    return render_template("score.html", score=score, num=num,)


# def score_2():
#     name = []
#     score2 = []
#     people = []
#     con2 = sqlite3.connect("movie.db")
#     cur2 = con2.cursor()
#     sql2 = "select cname,score,rated from movie250"
#     data2 = cur2.execute(sql2)
#     for item2 in data2:
#         name.append(item2[0])
#         score2.append(item2[1])
#         people.append(item2[2])
#     cur2.close()
#     con2.close()
#     return render_template("score.html", name=name, score2=score2, people=people)


@app.route('/wordcloud')
def wordcloud():
    return render_template("wordcloud.html")


@app.route('/other')
def other():
    return render_template("other.html")


if __name__ == '__main__':
    app.run()
