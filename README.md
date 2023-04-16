# Network Packet Classification with AI

This project helps classify network packets using artificial intelligence (AI) for better forensic analysis. It consists of a frontend application in folder cyai, a backend Python script in folder backend, and a server in folder server.

## Requirements

To run this project, you need to have the following software installed on your system:

- Node.js
- Python
- npm

## Installation

1. Clone the project repository to your local machine using the following command:

```
git clone https://github.com/svgvr8/AI-forensic-cybersecurity

```

2. Change the current working directory to folder backend using the following command:

```
cd backend
```

3. Create a virtual environment for the Python backend script using the following command:

```
python -m venv venv

```


4. Activate the virtual environment using the appropriate command for your operating system:

- On Unix-like systems:

  ```
  source venv/bin/activate
  ```

- On Windows:

  ```
  venv\Scripts\activate.bat
  ```

4. Install the Python dependencies using the following command:


```
pip install -r requirements.txt
```
5. ## Usage

Start the backend Python script by running the following command in folder backend:


```
python app.py

```
6. This will start the Python backend script, which uses machine learning algorithms to classify network packets.

Start the frontend by navigating to cyai folder and running the following command in folder server:

``` cd frontend ```

``` npm i ```

``` npm start ```


This will start the frontend, which provides an UI for the frontend application to interact with the Machine Learning Model.

7. Once the setup is done, you can simply run the code from the root folder using:

``` npm i ```
``` npm start ```

7. Upload network packet data to the frontend application and view the classification results. The frontend application provides a form for users to upload network packet data in the form of a PCAP file. Once the file is uploaded, the frontend application sends it to the server, which then sends it to the Python backend script for classification. The classification results are displayed in the frontend application for the user to view.

## Conclusion

That's it! You should now be able to use this project to classify network packets using AI for better forensic analysis. If you encounter any issues or have any questions, please refer to the project documentation or seek help from the project community.


