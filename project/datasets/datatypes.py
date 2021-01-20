import faker
import datetime


class FakeData:

    faker = faker.Faker()


class DataInteger(FakeData):

    def __init__(self, min_value = 0, max_value = 1000):
        self.min_value = min_value
        self.max_value = max_value

    def get_value(self):
        return self.faker.random_int(self.min_value, self.max_value)


class DataDate(FakeData):

    def __init__(self, start_date = '1970-01-01', end_date = '2034-01-01'):
        self.start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        self.end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

    def get_value(self):
        return self.faker.date_between_dates(self.start_date, self.end_date)


class DataText(FakeData):

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
