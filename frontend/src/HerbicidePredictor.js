import React, { useState } from 'react';
import axios from 'axios';

const HerbicidePredictor = () => {
  const [weedVariety, setWeedVariety] = useState('');
  const [applicationRate, setApplicationRate] = useState('');
  const [effectiveness, setEffectiveness] = useState('');
  const [predictedHerbicide, setPredictedHerbicide] = useState(null);
  const [error, setError] = useState(null);

  // Handle form submission
  const handleSubmit = async (event) => {
    event.preventDefault();

    // Validate input
    if (!weedVariety || !applicationRate || !effectiveness) {
      alert("All fields are required!");
      return;
    }

    const inputData = {
      Weed_Variety: weedVariety,
      Application_Rate: parseFloat(applicationRate),  // Ensure application rate is a number
      Effectiveness: parseFloat(effectiveness)       // Ensure effectiveness is a number
    };

    try {
      const response = await axios.post('http://localhost:5000/predictHerb', inputData);
      if (response.data.success) {
        setPredictedHerbicide(response.data.predicted_herbicide);
        setError(null);
      } else {
        setError("Prediction failed");
        setPredictedHerbicide(null);
      }
    } catch (err) {
      console.error("Error during prediction:", err);
      setError("Error during prediction");
      setPredictedHerbicide(null);
    }
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h2>Herbicide Prediction</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>
            Weed Variety:
            <input
              type="text"
              value={weedVariety}
              onChange={(e) => setWeedVariety(e.target.value)}
              required
            />
          </label>
        </div>
        <div>
          <label>
            Application Rate:
            <input
              type="text"
              value={applicationRate}
              onChange={(e) => setApplicationRate(e.target.value)}
              required
            />
          </label>
        </div>
        <div>
          <label>
            Effectiveness:
            <input
              type="text"
              value={effectiveness}
              onChange={(e) => setEffectiveness(e.target.value)}
              required
            />
          </label>
        </div>
        <button type="submit" style={{ marginTop: '20px' }}>Predict</button>
      </form>

      {/* Show prediction result */}
      {predictedHerbicide && (
        <div>
          <h3>Predicted Herbicide:</h3>
          <p>{predictedHerbicide}</p>
        </div>
      )}

      {/* Show error message */}
      {error && (
        <div style={{ color: 'red' }}>
          <h3>Error:</h3>
          <p>{error}</p>
        </div>
      )}
    </div>
  );
};

export default HerbicidePredictor;
