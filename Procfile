web: daphne LightApi.asgi:application --port $PORT --bind 0.0.0.0 -v2
chatworker: python manage.py runworker -settings=LightApi.settings -v2
