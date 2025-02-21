# MealBox-BackEnd
stack: python, django, drf

## Local development installation
1. At first pull the repository.

2. Create a virtual environment then activate it.
```bash
python3 -m venv "venv"
source venv/bin/activate
```

3. Install the required packages.
```bash
pip install -r backend/requirements/dev.txt
```

4. Run makemigrations command:
```bash
python manage.py makemigrations --settings=meal_box.settings.dev_settings
```

5. Run migrate command:
```bash
python manage.py migrate --settings=meal_box.settings.dev_settings
```

6. Run createsuperuser command:
```bash
python manage.py createsuperuser --settings=meal_box.settings.dev_settings
```

7. Run Project in Development mode:
```bash
python manage.py runserver --settings=meal_box.settings.dev_settings
```

Now click on this [URL](http://localhost:8000/admin/)  to check it works.
If you see a login page. Congratulations 👋. It works 🚀

## Contributing

1. Fork the project first.
2. Create a new branch from the development branch then send the pull request.
