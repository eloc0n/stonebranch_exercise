import csv

class Validator(object):
    ''' validate csv file data type and str length '''
    def validate_data_type(self, file_input, types):
        with open(file_input) as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader)
            for line in csv_reader:
                row = [data_type(value) for data_type, value in zip(types, line)]

    def validate_str_length(self, file_input, lengths):
        with open(file_input) as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader)
            for line in csv_reader:
                row = [len(value) for data_type, value in zip(lengths, line) \
                    if type(value) == str and len(value) <= data_type]