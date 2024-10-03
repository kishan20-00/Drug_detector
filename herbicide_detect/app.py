from flask import Flask, request, jsonify
import joblib
import pandas as pd
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load the saved model, label encoder, and one-hot encoded columns
model = joblib.load('logistic_regression_model.pkl')
label_encoder = joblib.load('label_encoder.pkl')
onehot_encoded_columns = joblib.load('onehot_encoder_columns.pkl')

# Define a route to handle predictions
@app.route('/predictHerb', methods=['POST'])
def predict():
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Extract input data (Weed_Variety, Application_Rate, Effectiveness) from JSON
        weed_variety = data['Weed_Variety']
        application_rate = data['Application_Rate']
        effectiveness = data['Effectiveness']

        # Create a DataFrame from the input data
        input_data = pd.DataFrame({
            'Weed_Variety': [weed_variety],
            'Application_Rate': [application_rate],
            'Effectiveness': [effectiveness]
        })

        # One-hot encode the input data using saved one-hot encoded column structure
        input_data_encoded = pd.get_dummies(input_data).reindex(columns=onehot_encoded_columns, fill_value=0)

        # Make the prediction using the loaded model
        predicted_class = model.predict(input_data_encoded)

        # Decode the predicted class back to the original herbicide name
        predicted_label = label_encoder.inverse_transform(predicted_class)

        # Return the predicted herbicide name as a JSON response
        return jsonify({
            'success': True,
            'predicted_herbicide': predicted_label[0]
        })
    
    except Exception as e:
        # Handle any errors during prediction
        return jsonify({
            'success': False,
            'error': str(e)
        })

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
