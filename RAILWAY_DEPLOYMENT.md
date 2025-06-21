# 🚂 Railway Deployment Guide for Ethiopian Places

This guide will help you deploy your Ethiopian Places Django project to Railway.

## 📋 Prerequisites

1. **Railway Account**: Sign up at [railway.app](https://railway.app)
2. **GitHub Account**: Your project is already on GitHub
3. **Git**: Already set up in your project

## 🚀 Deployment Steps

### Step 1: Sign Up for Railway
1. Go to [railway.app](https://railway.app)
2. Click "Start a New Project"
3. Sign up with your GitHub account (recommended)

### Step 2: Create New Project
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Choose your repository: `frtsh/Ethiopian-places-project`

### Step 3: Add PostgreSQL Database
1. In your Railway project dashboard
2. Click "New" → "Database" → "PostgreSQL"
3. Railway will automatically connect it to your app

### Step 4: Configure Environment Variables
In your Railway project settings, add these variables:

**Required Variables:**
```
SECRET_KEY=your-secret-key-here
DEBUG=False
```

**Optional Variables:**
```
PORT=8000
```

### Step 5: Deploy
Railway will automatically:
- Install dependencies from `requirements.txt`
- Run migrations (from railway.json)
- Collect static files
- Start your application with Gunicorn

### Step 6: Access Your App
Your app will be available at:
`https://your-app-name.railway.app`

## 🔧 Configuration Files

Your project includes these Railway-specific files:

- **`railway.json`**: Railway configuration and deployment commands
- **`requirements.txt`**: Production dependencies
- **`settings.py`**: Updated for Railway deployment
- **`Procfile`**: Alternative deployment method

## 🌐 Custom Domain (Optional)

1. In Railway dashboard, go to your app settings
2. Click "Custom Domains"
3. Add your domain (e.g., `ethiopianplaces.com`)
4. Configure DNS settings

## 📊 Monitoring

- **View logs**: In Railway dashboard → "Deployments" tab
- **Check app status**: Dashboard shows real-time status
- **Monitor database**: Database tab shows PostgreSQL info

## 🔄 Updating Your App

Railway automatically deploys when you push to GitHub:
1. Make changes to your code
2. Commit and push to GitHub
3. Railway automatically redeploys

## 🛠️ Troubleshooting

### Common Issues:

1. **Build fails**: Check `requirements.txt` for correct dependencies
2. **Database errors**: Check if PostgreSQL is connected
3. **Static files not loading**: Check `STATIC_ROOT` configuration
4. **App crashes**: Check logs in Railway dashboard

### Getting Help:
- Railway Documentation: [docs.railway.app](https://docs.railway.app)
- Django Deployment: [docs.djangoproject.com](https://docs.djangoproject.com/en/stable/howto/deployment/)

## 🎉 Success!

Once deployed, your Ethiopian Places website will be live on Railway and accessible to users worldwide!

## 💰 Pricing

- **Free Tier**: Available with generous limits
- **Pro Plan**: $5/month for additional resources
- **Team Plan**: $20/month for team collaboration

---

**Note**: Railway provides a modern, developer-friendly platform with excellent free tier options for Django applications. 