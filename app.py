from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    glucose = float(data['glucose'])
    bmi = float(data['bmi'])
    age = float(data['age'])

    # Simple mockup prediction logic
    if glucose > 120 and bmi > 25 and age > 40:
        prediction = "Positive for Diabetes"
    else:
        prediction = "Negative for Diabetes"

    return jsonify({'result': prediction})

if __name__ == '__main__':
    app.run(debug=True)
