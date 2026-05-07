release: python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn Busiwebproj.wsgi --log-file -