# BFIT Fitness Management System

BFIT is a Django web application for managing a gym's members, plans, trainer assignments, diet plans, complaints, feedback, and member/trainer chat. It also includes public fitness pages and workout guides.

## Project layout

- `Sample/` — Django project settings and root URL configuration
- `Guest/` — public pages, registration, and login
- `Admin/` — gym plans, trainers, member approvals, assignments, and administration
- `Trainer/` — assigned members, diet plans, complaints, and chat
- `User/` — member profile, admissions, feedback, complaints, chat, and workout pages
- `Basic/` — small calculator pages
- `Guest/static/Main/` — bundled styles, scripts, and fitness imagery

## Run locally

Use Python 3.12 or newer. From the project directory, create and activate a virtual environment, then install the dependencies:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Set a development signing key, create the local database tables, and start Django:

```powershell
$env:DJANGO_SECRET_KEY = (python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")
$env:DJANGO_DEBUG = "true"
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in a browser. User registration is available from the public site. To use the custom Admin area on a fresh database, create an initial Admin account through Django's shell:

```powershell
python manage.py shell
```

```python
from Admin.models import tbl_admin
tbl_admin.objects.create(
    admin_name="Local Admin",
    admin_email="admin@example.test",
    admin_password="replace-this-local-password",
)
```

The application currently uses custom plain-text password fields and a simulated payment flow. Use only disposable local accounts; this project needs authentication and payment hardening before public deployment. Set a stable `DJANGO_SECRET_KEY` in the environment for any deployed instance. The default secret is randomly generated at startup and will invalidate sessions when the process restarts.

`DEBUG` is off by default. The production Vercel hostname is allowed, Vercel's `VERCEL_URL` is added automatically when present, and extra hostnames can be supplied as a comma-separated `DJANGO_ALLOWED_HOSTS` environment variable.

## Deploy on Vercel

The default SQLite database is for local development. For a live Vercel deployment, connect a PostgreSQL provider such as Neon from the Vercel Marketplace and make its `DATABASE_URL` available to the Production environment. Django uses that URL automatically when it is set. Run `python manage.py migrate` against that database once before using the app; keep the database URL in Vercel's environment settings and out of Git.

## Local-only files

The SQLite database, virtual environments, Python caches, and uploaded media are excluded from Git. Run migrations to create a fresh database. Local profile uploads and chat attachments are stored under `media/` when using Django's development server.
