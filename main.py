# coding=utf-8

from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_text():
    if not request.json or not 'transcript' in request.json:
        abort(400)
    # Here we can do some processing on the text.
    # For now, return a static response.

    response = {
        'summary': 'It is a period of civil war. Rebel spaceships, striking from a hidden base, have won their first victory against the evil Galactic Empire. During the battle, Rebel spies managed to steal secret plans to the Empire’s ultimate weapon, the DEATH STAR, an armored space station with enough power to destroy an entire planet.',
        'keywords': 'rebel, empire'
    }
    return jsonify(response), 200

if __name__ == '__main__':
  app.run(debug=True)
