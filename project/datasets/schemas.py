import re
from . import datatypes

POST_DATA_REGEX = r'column_(?P<field_id>[1-9][0-9]*)_(?P<field_type>.+)'


def get_columns_info_from_schema_form(data):
    data = dict(data)
    columns = {}
    for k,v in data.items():
        mt = re.match(POST_DATA_REGEX, k)
        if not mt:
            continue
        field_id = mt.group('field_id')
        if not (field_id in columns):
            columns[field_id] = {}
        field_type = mt.group('field_type')
        columns[field_id][field_type] = v[0]
    return get_columns_info_from_columns(columns)

def get_columns_info_from_columns(columns):
    columns_info = []
    for column in columns.values():
        name = column['name']
        order = int(column['order'])
        datatype = column['type']
        datatype_class = datatypes.DATATYPES[datatype]
        params = []
        for parameter_name in datatype_class.html_input_parameters:
            if parameter_name in column:
                params.append(column[parameter_name])
            else:
                return None
        datatype = ','.join([datatype] + params)
        columns_info.append((name, order, datatype))
    return columns_info
