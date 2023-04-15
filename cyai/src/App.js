import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [inputText, setInputText] = useState('');
  const [classificationResult, setClassificationResult] = useState('');

  const classifyText = async () => {
    try {
      const response = await axios.post('http://localhost:5000/classify', {
        text: inputText,
      });

      setClassificationResult(response.data.result);
    } catch (error) {
      console.error('Error classifying text:', error);
    }
  };

  return (
    <div className="App">
      <h1>Malicious Text Classifier</h1>
      <textarea
        rows="10"
        cols="50"
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        placeholder="Enter text to classify"
      ></textarea>
      <br />
      <button onClick={classifyText}>Classify Text</button>
      {classificationResult && (
        <p>
          The text is <strong>{classificationResult}</strong>.
        </p>
      )}
    </div>
  );
}

export default App;
