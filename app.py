from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])


def index():
    password = ''
    
    if request.method == 'POST':
        length = int(request.form.get('length', 8))
        use_upper = request.form.get('uppercase') is not None
        use_lower = request.form.get('lowercase') is not None
        use_numbers = request.form.get('numbers') is not None
        use_symbols = request.form.get('symbols') is not None

        characters = ''
        if use_upper:
            characters += string.ascii_uppercase
        if use_lower:
            characters += string.ascii_lowercase
        if use_numbers:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        if characters:
            password = ''.join(random.choice(characters) for _ in range(length))
        else:
            password = 'Selecione ao menos uma opção.'

    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
