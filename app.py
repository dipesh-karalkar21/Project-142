from flask import Flask, jsonify
import csv
from storage import all_articles,liked,not_liked
from demographic import output
from content import get_recommendations

app = Flask(__name__)

@app.route("/get-article")
def getM():
    article = {
        'title' : all_articles[0][13],
        'url' : all_articles[0][12],
        'language' : all_articles[0][14],
        'text' : all_articles[0][15]
    }
    return jsonify({
        "Data" : all_articles,
        "status" : "success"
    }),201

@app.route("/liked",methods = ["POST"])
def getL():
    movie = all_articles[0]
    all_articles = all_articles[1:]
    liked.append(movie)
    return jsonify({
        "status" : "success"
    }),201

@app.route("/dliked",methods = ["POST"])
def getD():
    movie = all_articles[0]
    all_articles = all_articles[1:]
    not_liked.append(movie)
    return jsonify({
        "status" : "success"
    }),201

@app.route("/popular-articles")
def popular_movies():
    data = []
    for art in output:
        _d = {
            "title": art[0],
            "url": art[1],
            "language": art[2],
            "text": art[3],
        }
        data.append(_d)
    return jsonify({
        "data": data,
        "status": "success"
    }), 200


@app.route("/recommended-articles")
def recommended_articles():
    all_recommended = []
    for like in liked:
        output = get_recommendations(like[13])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    art_data = []
    for recommended in all_recommended:
        _d = {
            "title": recommended[0],
            "url": recommended[1],
            "lang": recommended[2],
            "text": recommended[3],
        }
        art_data.append(_d)
    return jsonify({
        "data": art_data,
        "status": "success"
    }), 200

app.run(debug = True)