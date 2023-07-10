answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

suitable_answers = ["42", 'forty two', 'forty-two']

if answer in suitable_answers:
    print("Yes")
else:
    print("No")