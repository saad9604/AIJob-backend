from flask import Flask, jsonify, request
from flask_cors import CORS

from gemini import search_jobs_with_gemini

app = Flask(__name__)
CORS(app)
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Gemini Web Search!"

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    query = data.get('query', '')
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    try:
        response_texts = search_jobs_with_gemini(query)
        response_texts = list(response_texts)  # Convert tuple to a list if needed
        if isinstance(response_texts[0], list):
            response_texts[0] = ', '.join(response_texts[0])  # Convert list to a comma-separated string
        return jsonify({"response_texts": response_texts[0]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)