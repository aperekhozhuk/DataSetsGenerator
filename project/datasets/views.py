from django.shortcuts import render, HttpResponseRedirect
from . import datatypes
from . import schemas
from .models import Schema, SchemaColumn


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
