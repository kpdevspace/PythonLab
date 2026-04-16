from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form.get('name', 'Student')
        return render_template('result.html', name=name)
    return render_template('form.html')


@app.route('/api/time')
def api_time():
    from datetime import datetime
    return jsonify({'time': datetime.utcnow().isoformat() + 'Z'})


if __name__ == '__main__':
    app.run(debug=True)
