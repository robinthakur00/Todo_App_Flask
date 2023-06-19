from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tasks = []  # List to store the tasks

# Custom filter to enable 'enumerate' in Jinja2 templates
@app.template_filter('enumerate')
def _enumerate(sequence, start=0):
    return enumerate(sequence, start=start)

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    tasks.append(task)
    return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
    if index < len(tasks):
        del tasks[index]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
