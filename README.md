# STB > Exercise

This is an exercise in order to evaluate the level of knowledge of a candidate.

# Structure

There are three .py files

### input.py

The core functionality resigns within here.

### helper.py

Here is checked the filename from user input.

### validator.py

Validates the data type within the a given csv file. 
(#Note: This just throws an error when data type is different from the one we specified.
It won't fix the wrong data value)

# How it works

First it asks from the user to type the filename with the customers sample data in it,
it performs a check as described above in helper.py.

Then it proceeds to run the first data type validation and if no errors are raised, 
validation of str type data comes after.

Upon data validation, the file is opened with csv module and the customers values are 
then stored in a set.

Since it has a set with all the customers to search for, now is the point where the search
from the three main csv files(CUSTOMER.csv, INVOICE.csv, INVOICE_ITEM.csv) begins.

The process that takes place is similar with the initial file read from the user input.
Data type and str length are performed in the beginning and afterwards each file is read
and a check happens in order to look data only for certain customers. As soon as it finds the 
related data, the writting process into new csv begins.


# Run
```
python3 input.py
```
# Input (uppercase)
```
CUSTOMER_SAMPLE
```
# or
```
CUSTOMER_SAMPLE.csv
```
