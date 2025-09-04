#  Shero Hub
Shero Hub is a beginner-friendly full-stack event management application.  
It allows users to register, log in, create events, and join or leave events.  
Both the frontend (React) and backend (Django + MongoDB) are organized in a single monorepo.

---

## Features
- JWT-based authentication (register/login with PyJWT)  
- User registration with hashed passwords (Django hashers)  
- Event management:
  - Create a new event (title, description, details, date, image)
  - View all events (public)
  - View single event details
  - Attend / Unattend events  
-  DRF browsable API for testing  
-  Clean fullstack architecture in a **single repo (monorepo)**  

---

## Technologies Used

### 🔙 Backend
- Python 3.11+  
- Django 5 + Django REST Framework  
- PyMongo (MongoDB Atlas)  
- PyJWT (JWT authentication)  
- django-cors-headers  
- python-dotenv  

### 🖥️ Frontend
- React + Vite  
- Tailwind CSS  
- React Router  
- Axios  
- Context API for auth state  

---

## Local Setup

### ✅ Prerequisites
- Python 3.11+  
- Node.js 18+  
- MongoDB Atlas account  
- Git  

---

## Installation

### 1) Clone the project
```bash
git clone https://github.com/Mfrydaki/shero_hub.git
cd shero_hub


### Backend Setup

i. Go to the backend folder and create a virtual environment:

```bash
cd my_events_backend
python -m venv venv

ii. Activate the virtual environment:

```bash
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate  

iii. Install dependencies:

```bash
pip install -r requirements.txt

iv. Create a .env file inside my_events_backend/:

SECRET_KEY=your_secret_key
DEBUG=True
MONGODB_URI=your_mongodb_atlas_uri
MONGODB_DB_NAME=my_events_backend
CORS_ALLOWED_ORIGINS=http://localhost:5173

v. Run the backend:

```bash
python manage.py runserver

DRF browsable API:
http://127.0.0.1:8000/events/


###Frontend Setup

i. Go to the frontend folder, install dependencies and run:

```bash
cd ../my_events_app
npm install
npm run dev

Default dev URLs:

Frontend → http://localhost:5173
Backend → http://127.0.0.1:8000

If needed, create .env inside my_events_app/:
VITE_API_BASE_URL=http://127.0.0.1:8000

### Folder Structure

shero_hub/
├── my_events_backend/   → Django backend (DRF + PyMongo)
├── my_events_app/       → React frontend
├── .gitignore
└── README.md

### Environment Variables

Backend (my_events_backend/.env):

SECRET_KEY=your_secret_key
DEBUG=True
MONGODB_URI=your_mongodb_atlas_uri
MONGODB_DB_NAME=my_events_backend
CORS_ALLOWED_ORIGINS=http://localhost:5173

Frontend (my_events_app/.env):


VITE_API_BASE_URL=http://127.0.0.1:8000


### API Endpoints

Auth

POST /auth/register/ → Register a new user
POST /auth/login/ → Login and receive JWT

Events

GET /events/ → List all events (public)
POST /events/ → Create a new event (requires JWT)
GET /events/:id/ → Get event details
POST /events/:id/attend/ → Attend an event (requires JWT)
POST /events/:id/unattend/ → Unattend an event (requires JWT)

