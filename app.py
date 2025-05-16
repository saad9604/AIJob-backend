import time
from flask import Flask, jsonify, request
from flask_cors import CORS

from duckduckgo import generate_three_queries, test_duckduckgo_search
from gemini import search_jobs_with_gemini

app = Flask(__name__)
CORS(app)
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Gemini Web Search!"

# @app.route('/duck', methods=['GET'])
# def duck():
#     data = test_duckduckgo_search()
#     return data

@app.route('/duck-gemini-search', methods=['POST'])
def duck_gemini_search():
    data = request.get_json()
    query = data.get('query', '')
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400
    try:
        response_texts = generate_three_queries(query)
        if response_texts.startswith("```"):
            response_texts = response_texts.split('\n', 1)[-1].rsplit('```', 1)[0].strip()
        try:
            response_texts_list = eval(response_texts)
        except (SyntaxError, NameError):
            response_texts_list = []
        response_texts_list = [text.strip() for text in response_texts_list if isinstance(text, str)]
        print("Formatted response_texts_list:", response_texts_list)
        query_results = []
        for idx, text in enumerate(response_texts_list):
            time.sleep(1)
            query_duckduckgo = test_duckduckgo_search(text)
            query_results.append(query_duckduckgo)
        return jsonify({"response_texts": query_results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


    


    
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