### How to run


- `source venv/bin/activate`
- `export APP_SETTINGS="config.DevelopmentConfig"`
- `python manage.py db upgrade` (if the database is not up to date)
- `python manage.py runserver`
- You may need to run postgres if it's not already running
