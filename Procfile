release: python manage.py makemigrations --noinput
release: python manage.py migrate --noinput
release: python manage.py collectstatic --noinput
web: daphne chat.asgi:channel_layer --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channels --settings=web_main.settings -v2
