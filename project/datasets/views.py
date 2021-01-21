from django.shortcuts import render, HttpResponseRedirect
from . import datatypes
from . import schemas


def index(request):
    return render(request, 'datasets/index.html',
                  context={'username': request.user.username})

def new_schema(request):
    if request.method == 'POST':
        data = request.POST
        columns = schemas.get_columns_info_from_schema_form(data)
        print(columns)
        return HttpResponseRedirect('/')


    new_schema_form_parameters = datatypes.DATATYPES_INPUT_PARAMETERS_JSON

    return render(
        request,
        'datasets/new_schema.html',
        context = {
            'new_schema_form_parameters' : new_schema_form_parameters,
        }
    )
