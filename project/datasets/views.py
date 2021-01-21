from django.shortcuts import render, HttpResponse,\
    HttpResponseRedirect, get_object_or_404
from . import datatypes
from . import schemas
from .models import Schema, SchemaColumn
from . import tasks


def index(request):
    return render(request, 'datasets/index.html',
                  context={'username': request.user.username})

def new_schema(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    if request.method == 'POST':
        data = request.POST
        schema_name = data['schema_name']
        columns = schemas.get_columns_info_from_schema_form(data)
        new_schema = Schema.objects.create(name = schema_name, user = request.user)
        for column in columns:
            name, order, datatype = column
            SchemaColumn.objects.create(
                name = name,
                datatype = datatype,
                order = order,
                schema = new_schema,
            )
        return HttpResponseRedirect('/')


    new_schema_form_parameters = datatypes.DATATYPES_INPUT_PARAMETERS_JSON

    return render(
        request,
        'datasets/new_schema.html',
        context = {
            'new_schema_form_parameters' : new_schema_form_parameters,
        }
    )

def schemas_list(request):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect('/login')
    user_schemas = user.schemas.all()
    data = [
        {
            'schema' : user_schema,
            'columns' : user_schema.columns.all()
        } for user_schema in user_schemas
    ]

    return render(
        request,
        'datasets/my_schemas.html',
        context = {
            'user_schemas' : data,
        }
    )

def generate_data(request):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect('/login')
    if request.method != 'POST':
        return HttpResponseRedirect('/')
    form = request.POST
    schema_id = form['schema_id']
    records_number = int(form['records_number'])
    schema = get_object_or_404(Schema, pk = schema_id)
    # If requested schema doesn't belong to authenticated user -
    # we need to block such request
    if schema.user.id != user.id:
        return HttpResponse(status = 403)
    # Finally, creating task
    tasks.create_task(schema, records_number)
    return HttpResponseRedirect('/')

def tasks_list(request):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect('/login')
    user_schemas = user.schemas.all()
    schemas_data = []
    for schema in user_schemas:
        name = schema.name
        tasks = list(schema.tasks.all())
        tasks_info = [
            {
                'id' : task.id,
                'records_number' : task.records_number,
                'finished' : task.finished,
            } for task in tasks
        ]
        schemas_data.append({
            'name' : name,
            'tasks' : tasks_info,
        })

    return render(
        request,
        'datasets/tasks_list.html',
        context = {
            'schemas_data' : schemas_data,
        }
    )
