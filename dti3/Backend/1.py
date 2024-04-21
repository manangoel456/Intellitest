from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

def parse_questions(file_content):
    questions = []
    question_texts = re.split(r'Q\d+\.', file_content)[1:]
    for q_text in question_texts:
        question = {}
        q_match = re.match(r'(.+?)Ans\.', q_text, re.DOTALL)
        if q_match:
            question['question'] = q_match.group(1).strip()
            options_match = re.findall(r'\(([A-E])\)(.*?)\n', q_text)
            options = [opt[1].strip() for opt in options_match]
            question['options'] = options
            ans_match = re.search(r'Ans\. \((\d+)\)', q_text)
            if ans_match:
                ans_index = int(ans_match.group(1)) - 1  # Convert to zero-based index
                if 0 <= ans_index < 10:
                    question['answer'] = chr(ord('A') + ans_index)
                else:
                    question['answer'] = None  # Invalid answer index
            else:
                question['answer'] = None  # No answer found
            questions.append(question)
    return questions

def write_questions(questions):
    with open('questions.txt', 'w') as f:
        for question in questions:
            f.write(question['question'] + '###')
            # for i, option in enumerate(question['options']):
            #     f.write(f"{chr(ord('A')+i)}) {option}\n")
            f.write('\n')

def write_answers(questions):
    with open('answers.txt', 'w') as f:
        for question in questions:
            if question['answer'] is not None:
                f.write(question['answer'] + '\n')
            else:
                f.write('No answer\n')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', message='No file selected')
        if file:
            content = file.read().decode('utf-8')
            questions = parse_questions(content)
            write_questions(questions)
            write_answers(questions)
            return redirect(url_for('mcqtest1'))  # Redirect to mcqtest1 route
    return render_template('index.html')

@app.route('/mcqtest1')
def mcqtest1():
    return render_template('redirect.html')

if __name__ == '__main__':
    app.run(debug=True)
