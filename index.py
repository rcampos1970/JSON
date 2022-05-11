from flask import Flask, render_template
import requests


def create_json(info, filename):
    appended_file = open(filename, "w")
    appended_file.write(str(info))


def append_json(info, filename):
    appended_file = open(filename, "a")
    appended_file.write(str(info))


file = "test_original.json"
page = "templates/api.html"
web_url_content = requests.get("https://rcampos1970.github.io/JSON/api").content
data = """
{
<pre>
"id": 6923,
"name": "timk",
"email": "timk@gmail.com",
"token": "4c563zlw-e2uz-3tl3-c92k-2y269zprjifj",
"country": UK,
"dob": 09/08/1978,
"userType": 2,
"userStatus": 0,       
}
</pre>
"""
create_json(web_url_content, file)
#append_json(data, page)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/api', methods=['GET', 'POST'])
def api():
    return render_template("api.html")


if __name__ == "__main__":
    app.run()
