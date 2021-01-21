from django.conf import settings
from .models import Task
from . import datatypes
import csv


def create_task(schema, records_number):
    task = Task.objects.create(schema = schema, records_number = records_number)
    run_task(task)

def run_task(task):
    schema = task.schema
    records_number = task.records_number
    columns = list(schema.columns.all())
    columns.sort(key = lambda obj : obj.order)
    data_generators = []
    for column in columns:
        column_datatype = column.datatype
        datatype_class, *parameters = column_datatype.split(',')
        datatype_class = datatypes.DATATYPES[datatype_class]
        html_input_parameters = list(datatype_class.html_input_parameters.values())
        if html_input_parameters:
            parameters_type = html_input_parameters[0]['type']
            if parameters_type == 'number':
                parameters = [int(p) for p in parameters]
        data_generators.append(datatype_class(*parameters))
    generate_csv(task.id, data_generators, records_number)
    task.finished = True
    task.save()

def generate_csv(file_id, data_generators, records_number):
    f = open(f'{settings.MEDIA_ROOT}/{file_id}.csv', 'w', newline='')
    writer = csv.writer(f)
    for i in range(records_number):
        row = [data_generator.get_value() for data_generator in data_generators]
        writer.writerow(row)
    f.close()
