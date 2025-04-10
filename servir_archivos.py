from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'timeline.html')

@app.route('/yearly_discoveries.json')
def timeline_data():
    return send_from_directory('.', 'yearly_discoveries.json')

if __name__ == '__main__':
    app.run(debug=True)