NESC Backend API

Overview
The NESC Backend API is a FastAPI-based project designed to provide an API for the NESC project. This API allows users to fetch violation data, which includes information like violation ID, location, latitude, longitude, and distance to buildings. The API supports CORS (Cross-Origin Resource Sharing), making it compatible with frontend applications hosted on different domains.

Features

GET /violations: Fetches a list of violations with details such as location, latitude, longitude, and distance to the building.

GET /: A basic root endpoint that returns a message indicating the API is working.

Installation

To set up the NESC Backend API on your local machine, follow these steps:

Clone the repository:

bash
Copy
Edit
git clone <repository_url>
Navigate into the project directory:

bash
Copy
Edit
cd nesc-backend
Set up a virtual environment:

bash
Copy
Edit
python -m venv venv
Activate the virtual environment:

On Windows:

bash
Copy
Edit
.\venv\Scripts\activate
On macOS/Linux:

bash
Copy
Edit
source venv/bin/activate
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Running the API Locally
Once you have set up the environment and installed dependencies, you can run the FastAPI server locally using:

bash
Copy
Edit
uvicorn main:app --reload
This will start the server at http://127.0.0.1:8000. You can then access the API at this address.

CORS Configuration

The API is configured to allow requests from specific origins. During development, it is set to allow requests from a React frontend running on http://localhost:3000. You can customize the allowed origins by modifying the origins list in the main.py file.

Deployment

The NESC Backend API is hosted on Render and can be accessed via the following URL:

https://apifrontend-e05x.onrender.com/
