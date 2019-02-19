import os
import config
from flask import Flask, request, render_template
from flask import redirect, url_for, session
from werkzeug import secure_filename
from modle import Admin, Article
from exts import db

UPLOAD_FOLDER = './static/image'
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']
app = Flask(__name__)


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = os.urandom(24)
app.config.from_object(config)
db.init_app(app)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# 发布图文
@app.route('/picture/', methods=['GET', 'POST'])
def upload_file():
    admin_id = session.get('user_id')
    if admin_id:
        if request.method == 'GET':
            return render_template('picture.html')
        else:
            file = request.files['file']
            content = request.form.get('content')
            if file:
                if allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                else:
                    return u'请按要求重新选择要上传的文件！'
            else:
                pass
            photo1 = Article(content = content, picture_path = file.filename)
            db.session.add(photo1)
            db.session.commit()
            return redirect(url_for('index'))
    else:
        return redirect(url_for('login_a'))

# 登录
@app.route('/login/', methods = ['POST', 'GET'])
def login_a():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = Admin.query.filter(Admin.telephone == telephone, Admin.password == password).first()
        if user:
            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('upload_file'))
        else:
            return u'账号或密码输入错误，请确认后重新输入！'

# 登出
@app.route('/logout/')
def logout_a():
    session.clear()
    return redirect(url_for('login_a'))

# 管理员欢迎界面
@app.route('/index/')
def index():
        return render_template('index.html')

# 注销
@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = Admin.query.filter(Admin.id == user_id).first()
        if user:
            return {'user': user}
    return {}

# 管理员直播入口
@app.route('/enter/')
def enter_a():
    return render_template('enter.html')

# 直播首页
@app.route('/')
def test():
    photo_all = Article.query.order_by('-create_time').all()
    content = {
        'photo': photo_all      # 获取所有数据
    }
    return render_template('test.html', **content)

# 图文管理
@app.route('/admin/list/', methods = ['GET', 'POST'])
def list_a():
    admin2_id = session.get('user_id')
    if admin2_id:
        if request.method == 'GET':
            data_all = Article.query.order_by('-create_time').all()
            items = {
                'photo': data_all
            }
            return render_template('list-admin.html', **items)
    else:
        return redirect(url_for('login_a'))

# 删除图文
@app.route('/remove/')
def remove():
    content = request.args.get('content')
    photo1 = Article.query.filter(Article.content == content).first()
    db.session.delete(photo1)
    db.session.commit()
    return redirect(url_for('list_a'))

# 查看图文
@app.route('/detail/<photo_id>/')
def detail_a(photo_id):
    photo_model = Article.query.filter(Article.id == photo_id).first()
    return render_template('detail.html', photo = photo_model)

# 修改图文
def allowed_file1(filename1):
    return '.' in filename1 and filename1.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/change/', methods = ['GET', 'POST'])
def change_a():
    admin3_id = session.get('user_id')
    if admin3_id:
        if request.method == 'GET':
            return render_template('change.html')
        else:
            file1 = request.files['file']
            content1 = request.form.get('content')
            photo_id = request.args.get('photo_id')
            if file1:
                if allowed_file(file1.filename):
                    filename = secure_filename(file1.filename)
                    file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                else:
                    return u'请按要求重新选择要上传的文件！'
            else:
                pass
            photo1 = Article.query.filter(Article.id == photo_id).first()
            if file1:
                photo1.picture_path = file1.filename
            if content1:
                photo1.content = content1
            db.session.commit()
            return redirect(url_for('list_a'))
    else:
        return redirect(url_for('login_a'))


if __name__ == '__main__':
    app.run(debug = True)