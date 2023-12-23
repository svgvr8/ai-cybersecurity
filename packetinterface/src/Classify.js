import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
	const [inputText, setInputText] = useState('');
	const [classificationResult, setClassificationResult] = useState('');
	const [confidence, setConfidence] = useState(null);
	const [loading, setLoading] = useState(false);

	const classifyText = async () => {
		try {
			setLoading(true);
			const response = await axios.post('http://localhost:5000/classify', {
				text: inputText,
			});

			setClassificationResult(response.data.result);
			setConfidence(response.data.confidence.toFixed(2));
		} catch (error) {
			console.error('Error classifying text:', error);
		} finally {
			setLoading(false);
		}
	};

	const copyToClipboard = (text) => {
		navigator.clipboard.writeText(text);
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
			{loading && <div className="loader"></div>}
			{classificationResult && (
				<p>
					The text is <strong>{classificationResult}</strong>.
					<br />
					Confidence: {confidence}
				</p>
			)}
			<div className="sample-text">
				<pre>Try: 47.597546	10.4.10.132	217.182.138.150	HTTP	392	GET /proforma/7yuebftyriq2gy6wq.exe HTTP/1.1</pre>
				<button onClick={() => copyToClipboard('47.597546\t10.4.10.132\t217.182.138.150\tHTTP\t392\tGET /proforma/7yuebftyriq2gy6wq.exe HTTP/1.1')}>Copy</button>
				<pre>Try: 42.262018	10.4.10.132	10.4.10.4	SMB2	126	Tree Disconnect Request</pre>
				<button onClick={() => copyToClipboard('42.262018\t10.4.10.132\t10.4.10.4\tSMB2\t126\tTree Disconnect Request')}>Copy</button>
			</div>
		</div>
	);
}

export default App;
