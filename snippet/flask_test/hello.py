#-*- coding:utf8 -*-
from flask import make_response,abort,redirect
from werkzeug import secure_filename
from flask import Flask,request,url_for
from flask import render_template

app = Flask(__name__)

@app.route('/notfound')
def errp():
    abort(401)

@app.route('/hello/') #绑定函数到对应的url
@app.route('/hello/<name>') #`<name>` 可以作为参数传给hello，支持三种类型：int、float、path
def hello(name=None):
    if name == 'error':
        print(url_for('hello'))
        return redirect(url_for('hello'))
    return render_template('hello.html', name=name)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/login', methods=['POST', 'GET'])
def login():
	print("lgoin")
	#print(request.method)
	error = None
	if request.method == 'POST':
		if valid_login(request.form['username'],request.form['password']):
		    return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # 如果请求访求是 GET 或验证未通过就会执行下面的代码
	return render_template('login.html', error=error)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id



if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
