# School CRM - Vercel Deployment

A Django-based School CRM application configured for deployment on Vercel.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/NimraJabbarr/deployment.git
cd deployment
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Variables
Create a `.env` file in the project root (see `.env.example`):
```bash
cp .env.example .env
```

For local development, set:
```
SECRET_KEY=your-development-secret-key
DEBUG=True
DATABASE_URL=postgresql://user:password@localhost:5432/school_crm
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Database Migration (Local)
```bash
python school_crm/manage.py migrate
```

### 6. Create Superuser (Local)
```bash
python school_crm/manage.py createsuperuser
```

### 7. Run Development Server
```bash
python school_crm/manage.py runserver
```

## Deployment to Vercel

### Prerequisites
- Vercel account
- Neon Database (or your PostgreSQL connection string)
- Git repository

### Steps

1. **Push code to GitHub**
   ```bash
   git add .
   git commit -m "Fix: Vercel deployment configuration"
   git push origin main
   ```

2. **Connect to Vercel**
   - Visit https://vercel.com/new
   - Import your GitHub repository
   - Select project root as the deployment directory

3. **Set Environment Variables in Vercel**
   Go to Project Settings → Environment Variables and add:
   
   - `SECRET_KEY`: Your Django secret key (generate a new one for production)
   - `DEBUG`: `False`
   - `DATABASE_URL`: Your Neon/PostgreSQL connection string
   - `ALLOWED_HOSTS`: Your Vercel domain (e.g., `yourapp.vercel.app`)
   - `CSRF_TRUSTED_ORIGINS`: https://yourapp.vercel.app
   - `SECURE_SSL_REDIRECT`: `True`
   - `SESSION_COOKIE_SECURE`: `True`
   - `CSRF_COOKIE_SECURE`: `True`

4. **Deploy**
   - Click "Deploy" and Vercel will:
     - Install dependencies from `requirements.txt`
     - Run `build.sh` which handles migrations and static file collection
     - Deploy your application

## Troubleshooting

### Static Files Not Loading
- Ensure `STATIC_ROOT` and `STATIC_URL` are correctly configured
- Check that `whitenoise` is installed and in `MIDDLEWARE`
- Verify static files were collected: `python manage.py collectstatic`

### Database Connection Errors
- Verify `DATABASE_URL` environment variable is set correctly
- Ensure database is accessible from Vercel (check IP allowlisting)
- For Neon DB, use the connection string from your Neon dashboard

### Secret Key Issues
- Generate a new SECRET_KEY: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`
- Update in Vercel environment variables

## Project Structure

```
deployment/
├── school_crm/           # Django project directory
│   ├── core/            # Main app
│   ├── school_crm/      # Project settings
│   ├── templates/       # HTML templates
│   ├── staticfiles/     # Collected static files
│   ├── manage.py        # Django management script
│   └── runtime.txt      # Python runtime version
├── requirements.txt     # Python dependencies
├── vercel.json         # Vercel configuration
├── build.sh            # Build script for Vercel
├── .env.example        # Environment variables template
├── .gitignore          # Git ignore rules
└── README.md          # This file
```

## Key Features

- ✅ Django 6.0 with REST Framework
- ✅ PostgreSQL Database Support
- ✅ Static File Management with WhiteNoise
- ✅ Vercel Serverless Deployment
- ✅ Environment Variable Management
- ✅ Security Best Practices

## License

MIT License
