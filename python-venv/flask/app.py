from flask import Flask
# https://pypi.org/project/Flask/1.0.2/

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello, World!!!'


if __name__ == '__main__':
	app.debug = True # デバッグモード有効化
	app.run()
##	app.run(host='0.0.0.0') # どこからでもアクセス可能に


# 実行方法
# $ FLASK_APP=app.py python3 -m flask run
#    or
# $ FLASK_APP=~/agaa-s/desk/app.py  /home/kunihiko/.local/bin/flask run
### $ FLASK_APP=~/git/desk/app.py ./flask run     /home/kunihiko/.local/bin
#    or
# 上記 11〜13行目のコメントをはずして
# $ python3 app.py
