import os

def check_correct_input(prompt):
    ''' in case we need to validate user input and probably check file path'''
    cwd = os.getcwd()
    while True:
        try:
            value = str(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if not '.csv' in value:
            value += '.csv'

        file_exists = os.path.exists(value)
        if not file_exists:
            print("Sorry, filename not found in your current path: ", cwd)
            continue
        else:
            break

    return value