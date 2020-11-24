"""
atomでデバッグするときは、
/home/kunihiko/agaa-s/desk/python-venv/flask で
activateした上で、shellからatomを実行する
$ . bin/activate
$ atom
※但し、一度Webサーバーを実行すると停止するすべがなさそう
"""
from flask import Flask

app = Flask(__name__)

'''
@ : デコレータ
[参考] https://qiita.com/mtb_beta/items/d257519b018b8cd0cc2e
       https://www.python.ambitious-engineer.com/archives/286
'''
@app.route('/') # ①
def hello():
	return 'Hello, World!!!'

"""
①は、hello()がcallされたときに呼び出されるのではなく
@app.route()の行の時点で呼び出されて、
継続するhello()を含め、関数オブジェクト形成した上で保持している。
但し、その関数オブジェクト自体は、hello()がcallされたときに実行される。
Flaskでは、関数オブジェクトとして保持する段階で、
app.route()の引数と継続する関数をマッピング情報として保持しているようだ。

agaa-s/desk/python-venv/flask/lib/python3.6/site-packages/flask/app.py：1288行目あたり
"""

# 実行方法 1)
# 下記のコメント(##)をはずして
# $ python3 app.py
## if __name__ == '__main__':
##	app.debug = True # デバッグモード有効化 -> reloadが有効になるなど
##	app.run()
###	app.run(host='0.0.0.0') # どこからでもアクセス可能に


# 実行方法 2)
# $ FLASK_APP=app.py python3 -m flask run
#    or
# $ FLASK_APP=app.py flask run

# [参考]
# https://pypi.org/project/Flask/1.1.2/
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application
