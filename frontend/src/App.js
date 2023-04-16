import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [inputText, setInputText] = useState('');
  const [classificationResult, setClassificationResult] = useState('');
  const [confidence, setConfidence] = useState(null);

  const classifyText = async () => {
    try {
      const response = await axios.post('http://localhost:5000/classify', {
        text: inputText,
      });

      setClassificationResult(response.data.result);
      setConfidence(response.data.confidence.toFixed(2));
    } catch (error) {
      console.error('Error classifying text:', error);
    }
  };

  return (
    <div className="App">
      <h1>Malicious Network Packet Classifier</h1>
      <textarea
        rows="10"
        cols="50"
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        placeholder="Enter text to classify"
      ></textarea>
      <br />
      <button onClick={classifyText}>Classify Packet</button>
      {classificationResult && (
        <p>
          The text is <strong>{classificationResult}</strong>.
          <br />
          Confidence: {confidence}
        </p>
      )}
    </div>
  );
}

export default App;
