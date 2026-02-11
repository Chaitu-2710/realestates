# Real Estate Web Application

A production-ready Real Estate Web Application built with Django, Tailwind CSS, and Alpine.js.

## Features

- **User Authentication**: Secure Login, Registration, and Logout.
- **Property Listings**: Browse properties with advanced filtering (Location, Price, Size).
- **Property Details**: View detailed information, image galleries, and location.
- **Inquiries**: Interested users can send inquiries directly from the property page.
- **Dashboard**: 
    - Track sent inquiries.
    - View saved properties.
    - Quick access to recently viewed properties.
- **Admin Panel**: customized interface for managing Properties, Users, and Inquiries.
- **Responsive Design**: Modern UI using Tailwind CSS, suitable for mobile and desktop.
- **Animations**: Smooth page transitions and element reveals using AOS (Animate On Scroll).

## Technology Stack

- **Backend**: Python 3.11+, Django 5.x
- **Database**: PostgreSQL (Production) / SQLite (Development)
- **Frontend**: Django Templates, Tailwind CSS, Alpine.js
- **Styling**: Tailwind CSS (via CDN for simplicity, or configured via npm)

## Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- (Optional) PostgreSQL installed and running

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd realestate
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   - Create a `.env` file in the root directory (same level as `manage.py`).
   - Use `.env.example` as a reference:
     ```
     DEBUG=True
     SECRET_KEY=your-secret-key-here
     DATABASE_URL=postgres://user:password@localhost:5432/realestate
     ALLOWED_HOSTS=localhost,127.0.0.1
     ```

5. **Apply Database Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create Superuser (Admin)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

   Access the application at `http://127.0.0.1:8000/`.

## Folder Structure

```
realestate/
├── accounts/          # User authentication and custom user model
├── core/              # Home page, contact, and shared views
├── dashboard/         # User dashboard (saved properties, inquiries)
├── inquiries/         # Inquiry logic and models
├── properties/        # Property management, listing, and searching
├── realestate/        # Project configuration (settings, urls, wsgi)
├── media/             # User-uploaded files (Property images)
├── static/            # Static assets (CSS, JS, Images)
├── templates/         # HTML Templates
├── manage.py          # Django command-line utility
└── requirements.txt   # Project dependencies
```

## Production Deployment Checklist

- [ ] Set `DEBUG=False` in `.env`.
- [ ] Configure `ALLOWED_HOSTS` with your domain name.
- [ ] Set up a production database (PostgreSQL recommended).
- [ ] Configure Static Files serving (e.g., using Whitenoise).
- [ ] Use Gunicorn as the WSGI server.
- [ ] Set up a reverse proxy (Nginx/Apache).
- [ ] Secure with SSL/HTTPS.
