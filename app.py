from flask import Flask
# https://pypi.org/project/Flask/1.0.2/

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello, World!!!'


if __name__ == '__main__':
	app.debug = True # デバッグモード有効化
	app.run()
#	app.run(host='0.0.0.0') # どこからでもアクセス可能に


# 実行方法
# $ FLASK_APP=app.py python3 -m flask run
#    or
# 上記コメントをはずして
# $ python3 app.py
