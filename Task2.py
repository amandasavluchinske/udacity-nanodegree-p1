"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def get_all_unique_phone_numbers():
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

    return list(set(phones_list))

def get_phone_and_time_with_highest_amount_of_seconds():
    highest_amount = 0
    phone_number = None

    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)
        for phone in get_all_unique_phone_numbers():
            amount_of_time_spent = 0
            for call in calls:
                if phone in [call[0], call[1]]:
                    amount_of_time_spent += int(call[3])
            if not amount_of_time_spent > highest_amount:
                continue
            highest_amount = amount_of_time_spent
            phone_number = phone
    return {"seconds": highest_amount, "phone": phone_number}

results = get_phone_and_time_with_highest_amount_of_seconds()

print(f"{results['phone']} spent the longest time, {results['seconds']} seconds, on the phone during September 2016.")
