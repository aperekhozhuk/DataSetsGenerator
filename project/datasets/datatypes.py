import faker
import datetime
import json


class FakeData:

    faker = faker.Faker()
    html_integer_input_parameters = {
        'type' : 'number',
        'step' : '1.0',
        'value' : 1,
    }
    html_date_input_parameters = {
        'type' : 'date',
        'value' : '2010-01-01',
    }
    html_input_parameters = []


class DataInteger(FakeData):

    html_input_parameters = {
        'min_value' : FakeData.html_integer_input_parameters,
        'max_value' : FakeData.html_integer_input_parameters,
    }

    def __init__(self, min_value = 0, max_value = 1000):
        self.min_value = min_value
        self.max_value = max_value

    def get_value(self):
        return self.faker.random_int(self.min_value, self.max_value)


class DataDate(FakeData):

    html_input_parameters = {
        'from' : FakeData.html_date_input_parameters,
        'to' : FakeData.html_date_input_parameters,
    }

    def __init__(self, start_date = '1970-01-01', end_date = '2034-01-01'):
        self.start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        self.end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

    def get_value(self):
        return self.faker.date_between_dates(self.start_date, self.end_date)


class DataText(FakeData):

    html_input_parameters = {
        'min_sentences' : FakeData.html_integer_input_parameters,
        'max_sentences' : FakeData.html_integer_input_parameters,
    }

    def __init__(self, min_sentences = 0, max_sentences = 10):
        self.min_sentences = min_sentences
        self.max_sentences = max_sentences

    def get_value(self):
        sentences_count = self.faker.random_int(
            self.min_sentences,
            self.max_sentences
        )
        return self.faker.paragraph(
            nb_sentences = sentences_count,
            variable_nb_sentences = False
        )


class DataFullName(FakeData):

    def get_value(self):
        return self.faker.name()


class DataJob(FakeData):

    def get_value(self):
        return self.faker.job()


class DataEmail(FakeData):

    def get_value(self):
        return self.faker.email()


class DataPhoneNumber(FakeData):

    def get_value(self):
        return self.faker.phone_number()


class DataAddress(FakeData):

    def get_value(self):
        return self.faker.address()


DATATYPES = {
    'Integer' : DataInteger,
    'Date' : DataDate,
    'Text' : DataText,
    'FullName' : DataFullName,
    'Job' : DataJob,
    'Email' : DataEmail,
    'PhoneNumber' : DataPhoneNumber,
    'Address' : DataAddress,
}

DATATYPES_INPUT_PARAMETERS = {}
for k, v in DATATYPES.items():
    DATATYPES_INPUT_PARAMETERS[k] = v.html_input_parameters

DATATYPES_INPUT_PARAMETERS_JSON = json.dumps(DATATYPES_INPUT_PARAMETERS)
