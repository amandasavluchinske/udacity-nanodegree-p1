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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A: Find all of the area codes and mobile prefixes called by people

def is_bangalore(call):
    return call[0:5] == '(080)'

def get_area_code(phone):
    if phone[0] == '(':
        return phone[1:].split(')', 1)[0]
    if phone[0] in [7, 8, 9]:
        return phone[0:3]
    if phone[0:3] == 140:
        return 140
    return None

def get_codes_called_by_people_in_bangalore():
    list_of_codes = []
    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)

        for call in calls:
            # Checks if first 5 chars of the number are (080)
            if is_bangalore(call[0]):
                code = get_area_code(call[1])
                if not code:
                    continue
                list_of_codes.append(code)
    return list(set(list_of_codes))

def print_out_list_of_codes():
    list_of_codes = get_codes_called_by_people_in_bangalore()
    list_of_codes.sort()
    print("The numbers called by people in Bangalore have codes:")
    for code in list_of_codes:
        print(code)

print_out_list_of_codes()


# Part B: What percentage of calls from fixed lines in Bangalore are made

def get_bangalore_bangalore_calls_percentage():
    b_calls = []
    bb_calls = []
    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)

        for call in calls:
            if is_bangalore(call[0]):
                b_calls.append(call)
                if is_bangalore(call[1]):
                    bb_calls.append(call)
    
    return round(float((len(bb_calls)/len(b_calls)) * 100), 2)

print(f"{get_bangalore_bangalore_calls_percentage()} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
                