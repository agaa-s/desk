from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello, World!!!'


# 実行方法 1)
# 下記のコメントをはずして
# $ python3 app.py
if __name__ == '__main__':
	app.debug = True # デバッグモード有効化 -> reloadが有効になるなど
	app.run()
##	app.run(host='0.0.0.0') # どこからでもアクセス可能に


# 実行方法 2)
# $ FLASK_APP=app.py python3 -m flask run
#    or
# $ FLASK_APP=app.py flask run

# 参考
# https://pypi.org/project/Flask/1.1.2/
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application
