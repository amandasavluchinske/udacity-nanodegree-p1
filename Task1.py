"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def get_all_phone_numbers():
    phones_list = []
    with open('texts.csv', 'r') as f:
        reader = csv.reader(f)
        texts = list(reader)
        for row in texts:
            phones_list.extend([row[0], row[1]])

    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)
        for row in calls:
            phones_list.extend([row[0], row[1]])

    return phones_list

def print_unique_phones_count(unique_phones_list):
    print(f"There are {len(unique_phones_list)} different telephone numbers in the records.")

print_unique_phones_count(list(set(get_all_phone_numbers())))
