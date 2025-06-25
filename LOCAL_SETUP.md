# Local Setup Guide for Ethiopian Places

## Running Locally

### 1. Setup Environment
```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

### 2. Database Setup
```bash
# Run migrations
python manage.py migrate

# Create superuser (for admin access)
python manage.py createsuperuser
```

### 3. Run Development Server
```bash
python manage.py runserver
```

Your site will be available at: `http://127.0.0.1:8000/`

### 4. Admin Dashboard
- Go to: `http://127.0.0.1:8000/admin/`
- Login with your superuser credentials
- Add/edit destinations manually

## Adding Data Locally

### Method 1: Admin Dashboard (Recommended)
1. Go to `http://127.0.0.1:8000/admin/`
2. Click on "Destinations"
3. Click "Add Destination"
4. Fill in:
   - Name: Destination name
   - Image: Upload an image file
   - Description: Detailed description
   - Price: Price in dollars
   - Offer: Check if it's on special offer
5. Click "Save"

### Method 2: Django Shell
```bash
python manage.py shell
```

```python
from frtuna.models import Destinations

# Add a destination
dest = Destinations(
    name="Lalibela",
    desc="Famous rock-hewn churches",
    price=2500,
    offer=True
)
dest.save()
```

## Railway Deployment (Static Files Only)

### 1. Push to GitHub
```bash
git add .
git commit -m "Update project"
git push origin main
```

### 2. Railway Configuration
- Railway will automatically detect your Django project
- It will serve your static files
- Database will be SQLite (local) or PostgreSQL (if configured)

### 3. Environment Variables (if needed)
In Railway dashboard, set:
- `DEBUG=False` (for production)
- `SECRET_KEY=your-secret-key`
- `DATABASE_URL=your-database-url` (if using external database)

## Project Structure

```
ethiopian_places/
├── frtuna/                 # Main app
│   ├── models.py          # Destinations model
│   ├── views.py           # Views
│   ├── admin.py           # Admin interface
│   └── urls.py            # URL patterns
├── templates/             # HTML templates
├── static/               # Static files (CSS, JS, images)
├── media/                # Uploaded images
└── manage.py             # Django management script
```

## Key Features

- ✅ Simple Django admin interface
- ✅ Image upload functionality
- ✅ Local development ready
- ✅ Railway deployment ready
- ✅ Static file serving
- ✅ Basic CRUD operations

## Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   python manage.py runserver 8001
   ```

2. **Database errors**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Static files not loading**
   ```bash
   python manage.py collectstatic
   ```

4. **Admin access issues**
   ```bash
   python manage.py createsuperuser
   ```

### Getting Help
- Check Django documentation
- Review error messages in terminal
- Check browser console for frontend issues
- Verify file permissions

## Next Steps

1. Add more destinations via admin
2. Customize templates
3. Add more features as needed
4. Deploy to Railway when ready

Your project is now back to a simple, clean state that runs locally and can be deployed to Railway for static file serving! 