echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@django.com', '1111')" | python project/manage.py shell
