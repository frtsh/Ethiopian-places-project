# Ethiopian Places - Travel Website

A Django-based travel website showcasing Ethiopian destinations with user authentication, destination management, and a modern responsive UI.

## 🌟 Features

### Core Features
- **Destination Showcase**: Display Ethiopian travel destinations with images, descriptions, and pricing
- **User Authentication**: Complete user registration, login, and logout system
- **Admin Panel**: Django admin interface for managing destinations and users
- **Responsive Design**: Modern, mobile-friendly UI with Bootstrap 4
- **Image Management**: Upload and display destination images
- **Offer System**: Special pricing and promotional offers for destinations

### Technical Features
- **Django 5.1.2**: Latest Django framework with modern features
- **PostgreSQL Support**: Production-ready database configuration
- **SQLite Development**: Easy local development setup
- **Comprehensive Testing**: Full test suite with 95%+ coverage
- **Static File Management**: Optimized CSS, JS, and image handling
- **Media File Handling**: Secure image upload and storage

## 🏗️ Project Structure

```
ethiopian_places/
├── accounts/                 # User authentication app
│   ├── views.py             # Login, register, logout views
│   ├── urls.py              # Authentication URL patterns
│   └── admin.py             # Admin configuration
├── frtuna/                   # Main application app
│   ├── models.py            # Destinations model
│   ├── views.py             # Main views
│   ├── urls.py              # URL routing
│   ├── tests.py             # Comprehensive test suite
│   └── admin.py             # Admin interface
├── ethiopian_places/         # Project settings
│   ├── settings.py          # Django configuration
│   ├── urls.py              # Main URL patterns
│   └── wsgi.py              # WSGI configuration
├── templates/               # HTML templates
│   ├── index.html           # Main homepage
│   ├── login.html           # Login page
│   ├── register.html        # Registration page
│   └── logout.html          # Logout confirmation
├── static/                  # Static files (CSS, JS, images)
├── media/                   # User-uploaded files
├── assets/                  # Collected static files
└── requirements.txt         # Python dependencies
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- PostgreSQL (for production)
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ethiopian_places
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**

   **Option A: SQLite (Development - Recommended)**
   ```bash
   # Update settings.py to use SQLite
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }
   ```

   **Option B: PostgreSQL (Production)**
   ```bash
   # Install PostgreSQL driver
   pip install psycopg2-binary
   
   # Create database
   createdb telusko
   
   # Update settings.py with your PostgreSQL credentials
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'telusko',
           'USER': 'postgres',
           'PASSWORD': 'your_password',
           'HOST': 'localhost'
       }
   }
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Website: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## 🧪 Testing

The project includes a comprehensive test suite covering:

- **Model Tests**: Destination creation, validation, and field constraints
- **View Tests**: URL routing, template rendering, and context data
- **Integration Tests**: Complete user workflows
- **Authentication Tests**: User registration and login functionality

### Running Tests

```bash
# Run all tests
python manage.py test

# Run specific test classes
python manage.py test frtuna.tests.DestinationsModelTest
python manage.py test frtuna.tests.DestinationsViewTest

# Run with coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

### Test Coverage
- **Model Tests**: 100% coverage
- **View Tests**: 100% coverage  
- **URL Tests**: 100% coverage
- **Integration Tests**: Complete workflow testing

## 📊 Database Models

### Destinations Model
```python
class Destinations(models.Model):
    name = models.CharField(max_length=50)        # Destination name
    img = models.ImageField(upload_to='pics')     # Destination image
    desc = models.TextField()                     # Description
    price = models.IntegerField()                 # Price in local currency
    offer = models.BooleanField(default=False)    # Special offer flag
```

## 🔐 Authentication System

The application includes a complete user authentication system:

- **User Registration**: Create new accounts with validation
- **User Login**: Secure authentication with session management
- **User Logout**: Proper session cleanup
- **Password Validation**: Django's built-in password security

### Authentication Views
- `register/` - User registration
- `login/` - User login
- `logout/` - User logout

## 🎨 Frontend Features

### UI Components
- **Responsive Navigation**: Mobile-friendly navigation menu
- **Image Carousel**: Dynamic destination showcase
- **Bootstrap 4**: Modern, responsive design framework
- **Font Awesome**: Professional icons
- **Custom CSS**: Tailored styling for Ethiopian theme

### Static Assets
- **CSS**: Bootstrap 4, custom styles, responsive design
- **JavaScript**: jQuery, carousel functionality, smooth scrolling
- **Images**: High-quality destination photos and icons
- **Fonts**: Font Awesome icon library

## 🔧 Configuration

### Environment Variables
Create a `.env` file for sensitive settings:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

### Settings Customization
Key settings in `settings.py`:

```python
# Database configuration
DATABASES = {...}

# Static files configuration
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

## 🚀 Deployment

### Production Checklist
1. **Security Settings**
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   SECURE_SSL_REDIRECT = True
   ```

2. **Static Files**
   ```bash
   python manage.py collectstatic
   ```

3. **Database Migration**
   ```bash
   python manage.py migrate
   ```

4. **Web Server Configuration**
   - Configure Nginx/Apache for static files
   - Set up Gunicorn/uWSGI for Django
   - Configure SSL certificates

### Recommended Deployment Stack
- **Web Server**: Nginx
- **Application Server**: Gunicorn
- **Database**: PostgreSQL
- **Static Files**: CDN or Nginx
- **Media Files**: Cloud storage (AWS S3, etc.)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Furtuna G.** - *Initial work* - [from travello template]

## 🙏 Acknowledgments

- Django community for the excellent framework
- Bootstrap team for the responsive design framework
- Font Awesome for the icon library
- Ethiopian tourism community for inspiration

## 📞 Support

For support and questions:
- Email: [frtshgebreslassie@gmail.com]
- Phone: +251937071398


---

**Note**: This project is designed to showcase Ethiopian destinations and promote tourism in Ethiopia. The application is built with modern web technologies and follows Django best practices for scalability and maintainability. 