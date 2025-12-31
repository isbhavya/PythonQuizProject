# quiz.py

from questions import questions

def run_quiz():
    score = 0

    print("\n🧠 Welcome to the Python Quiz!\n")

    for q in questions:
        print(q["question"])
        for opt in q["options"]:
            print(opt)

        user_answer = input("\nYour answer (A/B/C/D): ").strip().upper()

        if user_answer == q["answer"]:
            print("✔ Correct!\n")
            score += 1
        else:
            print(f"✘ Wrong! Correct answer is {q['answer']}\n")

    print(f"🎉 Quiz complete! Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()
