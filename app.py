from flask import Flask, jsonify
from feeds import fetch_threat_feeds
from ml_model import prioritize_threats

app = Flask(__name__)

@app.route('/threats', methods=['GET'])
def get_threats():
    # Fetch threat data from feeds and prioritize them using ML
    raw_data = fetch_threat_feeds()
    prioritized_data = prioritize_threats(raw_data)
    return jsonify(prioritized_data)

if __name__ == '__main__':
    app.run(debug=True)
