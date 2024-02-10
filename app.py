from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', defaults={'filename': 'file1.txt'})
@app.route('/<filename>')
def display_file(filename):
    try:
        file_path = os.path.join(os.getcwd(), filename)
        start_line = request.args.get('start_line')
        end_line = request.args.get('end_line')

        try:
            with open(file_path, 'r', encoding='utf-16') as f:
                lines = f.readlines()
        except UnicodeError:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()


        if start_line is not None and end_line is not None:
            start_line = max(1, int(start_line))
            end_line = min(len(lines), int(end_line))
            lines = lines[start_line - 1:end_line]
        elif start_line is not None:
            start_line = max(1, int(start_line))
            lines = lines[start_line - 1:]

        content = ''.join(lines)
        return render_template('file.html', content=content)
    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
