# Breast Cancer AI Detection System

## Project Description
This system detects breast cancer using AI and classifies medical images into three categories: Normal, Benign, and Malignant.

## Features
- User authentication (Login/Register)
- Upload medical images
- AI prediction using CNN model
- Patient management system
- Doctor dashboard

## Technologies Used
- Vue.js (Frontend)
- Flask (Backend)
- TensorFlow (Machine Learning)
- OpenCV (Image processing)
- SQLite (Database)

## How to Run Project

### Backend
1. Go to backend folder
2. Download the model from here.
3. Place the downloaded model in the "/saved_model" folder
4. Install dependencies:
   pip install -r requirements.txt
5. Run Flask:
   python app.py

### Frontend
1. Go to frontend folder
2. Install dependencies:
   npm install
3. Run project:
   npm run dev

## API Routes
- /login → User login
- /register → User registration
- /predict → AI prediction
- /patients → Patient data

## Author
Final Year Computer Science Project