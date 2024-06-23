from flask import Flask, request, jsonify
from flask_cors import CORS
from symptom_checker import check_symptoms

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from the frontend

@app.route('/api/check-symptoms', methods=['POST'])
def check_symptoms_api():
    data = request.get_json()
    symptoms = data.get('symptoms')
    recommendations = check_symptoms(symptoms)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
