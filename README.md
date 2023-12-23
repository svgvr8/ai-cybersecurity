# BrowserSOC: Network Security Tool with AI

An in-browser network security tool that uses machine learning classfication model to detect malicious activity. This app captures network data and auto analyzes them for security.

## Requirements

To run this project, you need to have the following software installed on your system:

- Node.js
- Python
- npm

## Installation

1. Clone the project repository to your local machine using the following command:

```
git clone https://github.com/svgvr8/BrowserSOC-AI-Network-Security

```

2. Change the current working directory to folder backend using the following command:

```
cd backend
```

3. Start the backend Python script by running the following command in folder backend:


```
python app.py

```
4. This will start the Python backend script, which uses machine learning algorithms to classify network packets.

Start the frontend by navigating to folder and running the following command in folder server:

``` cd packetinterface ```

``` npm i ```

``` npm start ```


This will start the frontend, which provides an UI for the frontend application to interact with the Machine Learning Model.

5. Upload network packet data to the frontend application and view the classification results. The frontend application provides a form for users to upload network packet data in the form of a PCAP file. Once the file is uploaded, the frontend application sends it to the server, which then sends it to the Python backend script for classification. The classification results are displayed in the frontend application for the user to view.

## Conclusion

That's it! You should now be able to use this project to classify network packets using AI for better forensic analysis. If you encounter any issues or have any questions, please refer to the project documentation or seek help from the project community.


