import flask
from flask import Flask, render_template, request, jsonify
from video import summary
from flask_cors import CORS, cross_origin

app = Flask(__name__)
#CORS(app)
#app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=["GET", "POST"])
#@cross_origin(origin='http://localhost:3000', headers=['Content- Type', 'application/json'])
def index():
    if request.method == "POST":
        content = request.get_json()
        data = content['data']
        print(content['data'])

        summary_data = summary(data)
        print(summary_data)
        return jsonify({'summary': summary_data})


if __name__ == '__main__':
    app.run(debug=True)
