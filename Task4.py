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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def does_not_send_or_receive_texts(phone):
    with open('texts.csv', 'r') as f:
        reader = csv.reader(f)
        texts = list(reader)

        for text in texts:
            if phone in [text[0], text[1]]:
                return False
    return True

def does_not_receive_calls(phone):
    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)

        for call in calls:
            if phone == call[1]:
                return False
    return True

def detect_telemarketers():
    possible_telemarketers = []
    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)

        for call in calls:
            if does_not_send_or_receive_texts(call[0]) and does_not_receive_calls(call[0]):
                possible_telemarketers.append(call[0])

    return list(set(possible_telemarketers))

def print_out_possible_telemarketers():
    possible_telemarketers = detect_telemarketers()
    possible_telemarketers.sort()

    print("These numbers could be telemarketers: ")
    for telemarketer in possible_telemarketers:
        print(telemarketer)

print_out_possible_telemarketers()
