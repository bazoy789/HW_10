from units import *
from flask import Flask

app = Flask(__name__)

@app.route('/')
def all():
    result = ''
    for i in get_all():
        result += i['name'] + '<br>'
        result += i['position'] + '<br>'
        result += i['skills'] + '<br>'
        result += '<br>'

    return f'<pre>{result}</pre>'


@app.route('/candidate/<int:pk>/')
def get_candidate(pk):
    candidate = get_by_pk(pk)
    result = ''
    result += candidate['name'] + '<br>'
    result += candidate['position'] + '<br>'
    result += candidate['skills'] + '<br>'

    return f'''<img src="{candidate["picture"]}">\n<pre>{result}</pre>'''


@app.route('/skill/<skill_name>/')
def get_skill(skill_name):
    candidate = get_by_skill(skill_name)
    result = ''
    for i in candidate:
        result += i['name'] + '<br>'
        result += i['position'] + '<br>'
        result += i['skills'] + '<br>'
        result += '<br>'
    return f'<pre>{result}</pre>'

if __name__ == '__main__':
    app.run()