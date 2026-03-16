# Quiz Engine System

import random  # used to shuffle the order of questions


# Function to load questions from the text file
def load_questions():
    questions = []  # empty list to store loaded questions

    # open the question file in read mode
    with open("question.txt", "r") as file:
        lines = file.readlines()

        # loop through the file lines and group them into question dictionaries
        for i in range(0, len(lines), 10):

            question = {
                # extract the question ID
                "id": int(lines[i].split(": ")[1].strip()),

                # extract the question text
                "question": lines[i + 1].split(": ")[1].strip(),

                # extract the four answer options
                "options": [
                    lines[i + 3].strip(),
                    lines[i + 4].strip(),
                    lines[i + 5].strip(),
                    lines[i + 6].strip()
                ],

                # extract the correct answer
                "answer": lines[i + 7].split(": ")[1].strip(),

                # extract the difficulty level
                "difficulty": lines[i + 8].split(": ")[1].strip()
            }

            # add the question dictionary to the list
            questions.append(question)

    # return the list of questions
    return questions


    # Function to allow the user to choose how many questions they want
def select_questions(questions):

    print("\nHow many questions would you like to answer?")
    print("1. 5 questions")
    print("2. 10 questions")
    print("3. 15 questions")
    print("4. All questions")

    choice = input("Enter your choice (1-4): ")

    # return a portion of the shuffled question list
    if choice == "1":
        return questions[:5]

    elif choice == "2":
        return questions[:10]

    elif choice == "3":
        return questions[:15]

    elif choice == "4":
        return questions

    else:
        print("Invalid choice. Defaulting to 5 questions.")
        return questions[:5]


        # Function that runs the quiz
def run_quiz(selected_questions):

    score = 0           # keeps track of correct answers
    wrong_list = []     # stores questions answered incorrectly

    # loop through each question
    for q in selected_questions:

        print("\n" + q["question"])

        # print the multiple choice options
        for option in q["options"]:
            print(option)

        # ask the user for their answer
        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        # validate the answer input
        while user_answer not in ["A", "B", "C", "D"]:
            user_answer = input("Invalid input. Please enter A, B, C, or D: ").upper()

        # check if the answer is correct
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            print("Correct answer:", q["answer"])

            # store wrong questions for results summary
            wrong_list.append((q["question"], q["answer"]))

    return score, wrong_list


    # Function to display quiz results
def display_results(score, total, wrong_list):

    incorrect = total - score
    percentage = (score / total) * 100

    # determine grade
    if percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "F"

    print("\n===== Quiz Results =====")
    print("Total Questions:", total)
    print("Correct Answers:", score)
    print("Incorrect Answers:", incorrect)
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)

    # show review of wrong questions
    if wrong_list:
        print("\nQuestions you got wrong:")

        for question, answer in wrong_list:
            print("Question:", question)
            print("Correct Answer:", answer)
            print()



            # Function to save player's score to the leaderboard
def save_leaderboard(name, score):

    # open leaderboard file in append mode
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name},{score}\n")


        # Main function to run the quiz program
def main():

    # load questions from file
    questions = load_questions()

    # shuffle the questions randomly
    random.shuffle(questions)

    # allow user to select number of questions
    selected_questions = select_questions(questions)

    # run the quiz
    score, wrong_list = run_quiz(selected_questions)

    # display results summary
    display_results(score, len(selected_questions), wrong_list)

    # ask user for their name
    name = input("\nEnter your name for the leaderboard: ")

    # save the score
    save_leaderboard(name, score)


# run the program
main()