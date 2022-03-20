import csv
from datetime import date

from helpers import check_correct_input
from validator import Validator

customer_file_input = 'CUSTOMER.csv'
invoice_file_input = 'INVOICE.csv'
invoice_item_file_input = 'INVOICE_ITEM.csv'

customer_file_output = 'output/{}'.format(customer_file_input)
invoice_file_output = 'output/{}'.format(invoice_file_input)
invoice_item_file_output = 'output/{}'.format(invoice_item_file_input)

validator = Validator()

def find_customers(file):
    types = [str, str, str]
    str_len = [30, 100, 100]
    validator.validate_data_type(customer_file_input, types)
    validator.validate_str_length(customer_file_input, str_len)
    with open(customer_file_input, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file, dialect='unix')
        with open(customer_file_output, 'w', newline='') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=csv_reader.fieldnames, \
                                    quotechar='"', quoting=csv.QUOTE_ALL)
            csv_writer.writeheader()
            for line in csv_reader:
                if line['CUSTOMER_CODE'] in file:
                    csv_writer.writerow(line)

def find_invoices(file):
    invoice_codes = []
    types = [str, str, float, date]
    str_len = [30, 30]
    validator.validate_data_type(invoice_file_input, types)
    validator.validate_str_length(invoice_file_input, str_len)
    with open(invoice_file_input, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file, dialect='unix')
        with open(invoice_file_output, 'w', newline='') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=csv_reader.fieldnames, \
                                    quotechar='"', quoting=csv.QUOTE_ALL)
            csv_writer.writeheader()
            for line in csv_reader:
                if line['CUSTOMER_CODE'] in file:
                    invoice_codes.append(line['INVOICE_CODE'])
                    csv_writer.writerow(line)

    return invoice_codes

def find_invoice_items(file):
    types = [str, str, float, int]
    str_len = [30, 30]
    validator.validate_data_type(invoice_item_file_input, types)
    validator.validate_str_length(invoice_item_file_input, str_len)
    with open(invoice_item_file_input, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file, dialect='unix')
        with open(invoice_item_file_output, 'w', newline='') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=csv_reader.fieldnames, \
                                    quotechar='"', quoting=csv.QUOTE_ALL)
            csv_writer.writeheader()
            for line in csv_reader:
                if line['INVOICE_CODE'] in file:
                    csv_writer.writerow(line)

def read_file(filename):
    ''' read csv file '''
    file_content = set()
    types = [str]
    str_len = [30]
    validator.validate_data_type(filename, types)
    validator.validate_str_length(filename, str_len)
    with open(filename, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file, dialect='unix')
        for line in csv_reader:
            file_content.add(line['CUSTOMER_CODE'])
            
    find_customers(file_content)
    file_content = find_invoices(file_content)
    find_invoice_items(file_content)


def main():
    filename = check_correct_input('Please type the filename: ')
    read_file(filename)

if __name__ == '__main__':
    main()