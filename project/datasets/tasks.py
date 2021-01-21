from .models import Task


def create_task(schema, records_number):
    Task.objects.create(schema = schema, records_number = records_number)
