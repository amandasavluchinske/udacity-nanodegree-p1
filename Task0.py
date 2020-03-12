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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

# First record of texts

def get_texts_from_csv():
    with open('texts.csv', 'r') as f:
        reader = csv.reader(f)
        texts = list(reader)
        return texts

def print_first_text_from_list(texts):
    first_text = texts[0]
    print(f"First record of texts, {first_text[0]} texts {first_text[1]} at time {first_text[2]}")

print_first_text_from_list(get_texts_from_csv())

# Last record of calls

def get_calls_from_csv():
    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)
        return calls

def print_last_call_from_list(calls):
    last_call = calls[-1]
    print(f"Last record of calls, {last_call[0]} calls {last_call[1]} at time {last_call[2]}, lasting {last_call[3]} seconds")

print_last_call_from_list(get_calls_from_csv())
