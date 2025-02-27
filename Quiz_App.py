import random
import time

# List of questions and answers
questions = [
    {"question": "What is the output of the following code?\nprint(2 ** 3)", "choices": ["A. 6", "B. 8", "C. 9", "D. 12"], "answer": "B"},
    {"question": "Which of the following is a mutable data type in Python?", "choices": ["A. Tuple", "B. String", "C. List", "D. Integer"], "answer": "C"},
    {"question": "What is the correct syntax to create a function in Python?", "choices": ["A. def functionName():", "B. function functionName()", "C. create function functionName()", "D. functionName()"], "answer": "A"},
    {"question": "How do you insert an element at the end of a list in Python?", "choices": ["A. list.add(element)", "B. list.append(element)", "C. list.insert(element)", "D. list.push(element)"], "answer": "B"},
    {"question": "What is the output of the following code?\nx = [1, 2, 3]\nprint(x[1])", "choices": ["A. 1", "B. 2", "C. 3", "D. Error"], "answer": "B"},
    {"question": "Which of the following is used to handle exceptions in Python?", "choices": ["A. try and except", "B. catch and throw", "C. handle and except", "D. try and catch"], "answer": "A"},
    {"question": "What is the output of the following code?\nfor i in range(3):\n    print(i)", "choices": ["A. 0 1 2", "B. 1 2 3", "C. 0 1 2 3", "D. 1 2 3 4"], "answer": "A"},
    {"question": "Which of the following methods can be used to remove whitespace from the beginning and end of a string in Python?", "choices": ["A. strip()", "B. trim()", "C. remove()", "D. delete()"], "answer": "A"},
    {"question": "What is the output of the following code?\nx = {'a': 1, 'b': 2}\nprint(x['a'])", "choices": ["A. 1", "B. 2", "C. 'a'", "D. Error"], "answer": "A"},
    {"question": "Which of the following is the correct way to import a module in Python?", "choices": ["A. import module", "B. include module", "C. require module", "D. using module"], "answer": "A"}
]

# Shuffle the questions to randomize the order
random.shuffle(questions)
score = 0

# Start the timer
start_time = time.time()

# Loop through each question
for q in questions:
    print(q["question"])
    for choice in q["choices"]:
        print(choice)
    answer = input("Your answer: ")
    if answer.upper() == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {q['answer']}.")
    print()

# End the timer
end_time = time.time()

# Display the final score and time taken
print(f"Your final score is: {score}/{len(questions)}")
print(f"Time taken: {end_time - start_time} seconds")