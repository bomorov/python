
def question_method(question: str, answer: str):
    input_value = f"{input(question)}"
    print(f"{answer} {input_value}")

question_method("What is your name? ", "Hello ")
question_method("How old are you? ", "You are ") 