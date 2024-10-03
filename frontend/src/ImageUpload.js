import React, { useState } from 'react';
import axios from 'axios';

const ImageUpload = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [imagePreview, setImagePreview] = useState(null);
  const [predictedClass, setPredictedClass] = useState(null);
  const [error, setError] = useState(null);

  // Handle file input change
  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);

    // Preview image before upload
    const reader = new FileReader();
    reader.onloadend = () => {
      setImagePreview(reader.result);
    };
    reader.readAsDataURL(file);
  };

  // Handle form submission
  const handleSubmit = async (event) => {
    event.preventDefault();
    
    if (!selectedFile) {
      alert("Please select an image!");
      return;
    }

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      const response = await axios.post('http://localhost:5000/predict', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });

      // Assuming the Flask app returns JSON with a predicted_class key
      if (response.data.predicted_class) {
        setPredictedClass(response.data.predicted_class);
        setError(null);
      } else {
        setError("Prediction failed");
        setPredictedClass(null);
      }
    } catch (error) {
      console.error("There was an error uploading the image!", error);
      setError("Error uploading image");
    }
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h2>Upload an Image for Prediction</h2>
      
      <form onSubmit={handleSubmit}>
        <input type="file" accept="image/*" onChange={handleFileChange} />
        <button type="submit" style={{ marginTop: '20px' }}>Submit</button>
      </form>

      {/* Preview the selected image */}
      {imagePreview && (
        <div>
          <h3>Image Preview:</h3>
          <img src={imagePreview} alt="Preview" style={{ width: '300px', marginTop: '20px' }} />
        </div>
      )}

      {/* Show prediction result */}
      {predictedClass && (
        <div>
          <h3>Predicted Class:</h3>
          <p>{predictedClass}</p>
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

export default ImageUpload;
