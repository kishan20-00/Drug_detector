import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ImageUpload from './ImageUpload';  // The new page
import HerbicidePredictor from './HerbicidePredictor'; 

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/weed-detect" element={<ImageUpload />} />
        <Route path="/herbicide-predictor" element={<HerbicidePredictor />} />
      </Routes>
    </Router>
  );
}

export default App;
