import random

def load_questions():
    questions = []
    
    with open("question.txt", "r") as file:
        lines = file.readlines()

        for i in range(0, len(lines), 10):
            question = {
                "id": int(lines[i].split(": ")[1].strip()),
                "question": lines[i + 1].split(": ")[1].strip(),
                "options": [
                    lines[i + 3].strip(),
                    lines[i + 4].strip(),
                    lines[i + 5].strip(),
                    lines[i + 6].strip()
                ],
                "answer": lines[i + 7].split(": ")[1].strip(),
                "difficulty": lines[i + 8].split(": ")[1].strip()
            }

            questions.append(question)

    return questions