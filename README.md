
# Shero Hub

Shero Hub is a full-stack event management application built as a personal software development project.

The application allows users to register, log in, explore events, create events, and attend or leave events.

The frontend and backend are organized in a single repository.

## Features

- User registration and login
- JWT-based authentication using PyJWT
- Secure password hashing with Django
- Create events with a title, description, details, date, and image
- Browse available events
- View individual event details
- Attend and unattend events
- REST API connecting the frontend and backend
- MongoDB database integration

## Technologies Used

### Backend

- Python 3.11+
- Django 5
- Django REST Framework
- PyMongo
- MongoDB Atlas
- PyJWT
- django-cors-headers
- python-dotenv

### Frontend

- React
- Vite
- JavaScript
- Tailwind CSS
- React Router
- Axios
- Context API

## Local Setup

### Prerequisites

Before running the project, make sure you have:

- Python 3.11+
- Node.js 18+
- Git
- A MongoDB Atlas account

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Mfrydaki/Shero-hub-App.git
cd Shero-hub-App
```

### 2. Backend Setup

Open a terminal and navigate to the backend folder:

```bash
cd my_events_backend
```

Create a Python virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

On macOS/Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file inside `my_events_backend/` and add the following variables:

```env
SECRET_KEY=your_secret_key
DEBUG=True
MONGODB_URI=your_mongodb_atlas_uri
MONGODB_DB_NAME=my_events_backend
CORS_ALLOWED_ORIGINS=http://localhost:5173
```

Replace the placeholder values with your own configuration.

Never upload real passwords, API keys, or database credentials to GitHub.

Start the Django development server:

```bash
python manage.py runserver
```

The backend should be available at:

http://127.0.0.1:8000

DRF browsable API:

http://127.0.0.1:8000/events/

### 3. Frontend Setup

Keep the backend server running.

Open a new terminal in the root folder of the project and navigate to the frontend directory:

```bash
cd my_events_app
```

Install the frontend dependencies:

```bash
npm install
```

Create a `.env` file inside `my_events_app/`:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

Start the frontend development server:

```bash
npm run dev
```

The frontend should be available at:

http://localhost:5173

### 4. Local Development URLs

| Service | URL |
|---------|-----|
| Frontend | http://localhost:5173 |
| Backend | http://127.0.0.1:8000 |
| Events API | http://127.0.0.1:8000/events/ |

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register/` | Register a new user |
| POST | `/auth/login/` | Log in and receive a JWT |
| GET | `/auth/profile/` | Retrieve authenticated user profile |

### Events

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/events/` | List all events |
| POST | `/events/` | Create a new event |
| GET | `/events/:id/` | View event details |
| POST | `/events/:id/attend/` | Attend an event |
| POST | `/events/:id/unattend/` | Leave an event |

Protected endpoints require JWT authentication.

## Project Structure

```text
Shero-hub-App/
├── my_events_backend/    # Django backend
├── my_events_app/        # React frontend
├── screenshots/          # Application screenshots
├── .gitignore
└── README.md
```

## Environment Variables

The application uses environment variables to manage configuration.

Backend:

```env
SECRET_KEY=your_secret_key
DEBUG=True
MONGODB_URI=your_mongodb_atlas_uri
MONGODB_DB_NAME=my_events_backend
CORS_ALLOWED_ORIGINS=http://localhost:5173
```

Frontend:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

The `.env` files should remain local and must not be committed to the repository.


## About This Project

I developed Shero Hub as my final project for the Coding Factory Software Development Bootcamp at Athens University of Economics and Business (AUEB).

The project gave me the opportunity to put what I had learned into practice by building a full-stack application from scratch.

Through this experience, I worked with frontend and backend development, REST APIs, user authentication, and database integration.



