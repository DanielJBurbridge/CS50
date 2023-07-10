import re

banks_greeting = input("Greeting: ").strip().lower()

responses = ["^hello.*", "^h.*"]

matrix = []

for response in responses:
    matrix.append(bool(re.match(response, banks_greeting)))


if matrix[0]:
    print("$0")
    exit()
if matrix[1]:
    print("$20")
    exit()

print("$100")




