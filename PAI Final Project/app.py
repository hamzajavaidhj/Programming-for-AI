# app.py

from flask import Flask, render_template, request
from model import get_best_answer

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    best_answer = None
    similar_answers = []
    if request.method == 'POST':
        question = request.form['question']
        best_answer, similar_answers = get_best_answer(question)
    return render_template('index.html', best_answer=best_answer, similar_answers=similar_answers)

if __name__ == '__main__':
    app.run(debug=True)
