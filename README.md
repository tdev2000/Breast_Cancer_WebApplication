# Breast Cancer Detection Web Application (AI System)

## 📌 Project Overview
This project is a web-based AI system that detects breast cancer from ultrasound images. It classifies images into three categories: Normal, Benign, and Malignant using a CNN model. The system is built using Flask (backend) and Vue.js (frontend).

---

## 🛠️ Technologies Used

### Backend
- Python 3.11.4
- Flask
- Flask-CORS
- TensorFlow
- OpenCV
- NumPy
- Pandas
- Scikit-learn
- Pillow
- Werkzeug

### Frontend
- Vue.js
- JavaScript
- HTML/CSS

### Database
- SQLite

---

## 📁 Project Structure

backend/
│── app.py  
│── model/  
│── database/  
│── requirements.txt  

frontend/
│── src/  
│   ├── views/  
│   ├── components/  
│   ├── router/  
│── package.json  

---

## ⚙️ Installation & Setup

### 1. Clone Repository
git clone <your-repo-link>  
cd project-folder  

---

### 2. Backend Setup

cd backend  
python -m venv venv  

Activate venv:

Windows:
venv\Scripts\activate  

Mac/Linux:
source venv/bin/activate  

Install dependencies:
pip install -r requirements.txt  

Run backend:
python app.py  

---

### 3. Frontend Setup

cd frontend  
npm install  
npm run dev  

---

## 📊 Model Training (Jupyter Notebook)

- Create virtual environment (venv)
- Install required libraries
- Open Jupyter Notebook
- Load dataset (normal, benign, malignant)
- Preprocess images (resize, normalize, label encoding)
- Train CNN model
- Evaluate model performance
- Save model as .h5 file
- Move model to backend/model/

---

## 🔗 API Endpoints

POST /register → User registration  
POST /login → User login  
POST /predict → Image prediction  
GET /patients → Get patient data  
PUT /patients/:id → Update patient  
DELETE /patients/:id → Delete patient  

---

## 🚀 Features

- User authentication system
- Medical image upload
- AI-based prediction system
- Patient management system
- Doctor dashboard
- Real-time prediction results

---

## 🧠 Machine Learning Model

- CNN (Convolutional Neural Network)
- Input: 224×224 images
- Output: Normal / Benign / Malignant
- Framework: TensorFlow

---

## 📌 How to Run

1. Start backend (Flask)
2. Start frontend (Vue)
3. Open browser:
http://localhost:5173

---

## 👨‍💻 Author
Final Year Computer Science Project

---

## 📄 Notes
- Backend must run before frontend
- Model file must be inside backend/model/
- All dependencies must be installed before running