from flask import Flask, render_template, request, redirect
from models import Question, Result

app = Flask(__name__, template_folder='assignment 4/templete')

# Stack (LIFO)
questions_stack = [
    Question("Capital of Nigeria?", ["Abuja", "Lagos", "Kano"], "Abuja"),
    Question("2 + 2?", ["3", "4", "5"], "4"),
    Question("Color of sky?", ["Blue", "Green", "Red"], "Blue")
]

user_answers = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        answer = request.form['answer']
        user_answers.append(answer)

        if questions_stack:
            questions_stack.pop()

    if not questions_stack:
        return redirect('/result')

    current_question = questions_stack[-1]
    return render_template('quiz.html', question=current_question)

@app.route('/result')
def result():
    score = 0
    total = len(user_answers)

    # Recreate questions to check answers
    original_questions = [
        Question("Capital of Nigeria?", ["Abuja", "Lagos", "Kano"], "Abuja"),
        Question("2 + 2?", ["3", "4", "5"], "4"),
        Question("Color of sky?", ["Blue", "Green", "Red"], "Blue")
    ]

    for i in range(total):
        if original_questions[i].check_answer(user_answers[i]):
            score += 1

    result = Result(score, total)

    return render_template('result.html', result=result.get_result())

if __name__ == '__main__':
    app.run(debug=True)