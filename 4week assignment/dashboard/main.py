from flask import Flask, render_template, request, redirect, flash, send_from_directory
from flask_login import login_user, current_user, logout_user, LoginManager, login_required
from mysql import connect_mysqldb
from user import User
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'C:\\Users\\evan1\\OneDrive\\바탕 화면\\hacking study\\P4C\\dashboard\\Upload_folder\\'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'session'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    # 로그인되어 있지 않은 사용자일 경우 첫화면으로 이동
    return redirect("/")

#처음 화면
@app.route('/')
def index():
    #db에서 게시글들 가져오기
    db = connect_mysqldb()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM posts')
    posts = cursor.fetchall()
    return render_template('index.html', posts=posts) #html파일의 posts로 지금 파일의 posts변수 전달

#게시글 조회
@app.route('/<int:idx>')
def view_idx(idx):
    db = connect_mysqldb()
    cursor = db.cursor()
    #라우팅 경로에 쓰여진 idx값을 가진 게시물 가져오기
    cursor.execute(f'SELECT * FROM posts WHERE idx={idx}')
    idx_post = cursor.fetchone()
    return render_template('view_idx.html', post=idx_post) 

#게시물 생성
@app.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    db = connect_mysqldb()
    cursor = db.cursor()
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        file = request.files['file']
        is_secret = request.form['is_secret']
        
        
        # 파일이 업로드된 경우 저장
        if file:
            filename = secure_filename(file.filename)
            file.save(app.config['UPLOAD_FOLDER']+secure_filename(file.filename))
            cursor.execute("INSERT INTO posts (title, content, is_secret, file_name, user_name) VALUES (%s, %s, %s, %s, %s)", (title, content, is_secret, filename, current_user.id))
        else:
            cursor.execute("INSERT INTO posts (title, content, is_secret, user_name) VALUES (%s, %s, %s, %s)", (title, content, is_secret, current_user.id))
        db.commit()
        
        if is_secret == '1':
            return redirect('/post_password')
        
        
        # 게시물 생성이 끝나면 처음 페이지로 돌아가기
        return redirect('/')
    return render_template('create.html')

#게시물 업데이트
@app.route('/<int:idx>/update', methods=['GET', 'POST'])
@login_required
def update(idx):
    db = connect_mysqldb()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM posts WHERE idx=%s", idx)
    post = cursor.fetchone()
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        cursor.execute("UPDATE posts SET title=%s, content=%s WHERE idx=%s", (title, content, idx))
        db.commit()
        return redirect('/')
    return render_template('update.html', post=post)
    
# 게시물 검색    
@app.route('/search', methods= ['GET', 'POST'])
def search():
    db = connect_mysqldb()
    cursor = db.cursor()
    if request.method == 'POST':
        cursor.execute("SELECT * FROM posts")
        posts = cursor.fetchall()
        search_type = request.form['type']
        search = request.form['search']
        search_posts = list()
        if search_type == 'entire':
            for post in posts:
                if post[1].find(search) != -1 or post[2].find(search) != -1:
                    search_posts.append(post)
        elif search_type == 'title':
            for post in posts:
                if post[1].find(search) != -1:
                    search_posts.append(post)
        else:
            for post in posts:
                if post[2].find(search) != -1:
                    search_posts.append(post)
        return render_template('search.html', posts = search_posts)
    return render_template('search.html', posts = None)

#게시물 삭제
@app.route('/<int:idx>/delete', methods=['GET', 'POST'])
def delete(idx):
    db = connect_mysqldb()
    cursor = db.cursor()
    cursor.execute("DELETE FROM posts WHERE idx=%s", idx)
    db.commit()
    return redirect('/')

#계정 만들기
@app.route('/register', methods =['GET', 'POST'])
def register():
    db = connect_mysqldb()
    cursor = db.cursor()
    cursor.execute('SELECT user_id from user_info')
    exist_userids = cursor.fetchall()
    if request.method == 'POST':
        user_id = request.form['user_id']
        user_pw = request.form['user_pw']
        user_name = request.form['user_name']
        user_email = request.form['user_email']
        user_phonenum = request.form['user_phonenum']
        cursor.execute("INSERT INTO user_info (user_id,user_pw,user_name,user_email,user_phonenum) VALUES (%s, %s, %s, %s, %s)", (user_id, user_pw,user_name,user_email,user_phonenum))
        db.commit()
        return redirect('/')
    return render_template('register.html')

#로그인
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        id = request.form['id']
        pw = request.form['pw']
        user = user = User.get(id)
        if user.pw == pw:
            login_user(user)
            return redirect('/') 
        
    return render_template('login.html')

#로그아웃
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')


#파일 다운로드
@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

#비밀글 비밀번호 입력
@app.route('/post_password', methods=['GET', 'POST'])
def post_password():
    db = connect_mysqldb()
    cursor = db.cursor()
    if request.method == 'POST':
        post_password = request.form['post_password']
        cursor.execute("SELECT MAX(idx) FROM posts WHERE user_name=%s", (current_user.id))
        idx = cursor.fetchone()
        cursor.execute("UPDATE posts SET post_password=%s WHERE idx=%s", (post_password, idx))
        db.commit()
        return redirect('/')
    return render_template('post_password.html')

#비밀글 비밀번호 입력 시 게시글 조회
@app.route('/<int:idx>/input_password', methods=['GET', 'POST'])
def input_password(idx):
    db = connect_mysqldb()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM posts WHERE idx=%s", (idx))
    post = cursor.fetchone()
    post_password = post[4]
    if request.method == 'POST':
        input_password = request.form['input_password']
        if post_password == input_password:
            return_str = f'/{idx}'
            return redirect(return_str)
        else:
            flash('비밀번호 불일치')
            return render_template('error_flash.html')
    return render_template('input_password.html',idx=idx)

#아이디 찾기
@app.route('/find_id', methods=['GET', 'POST'])
def find_id():
    if request.method == 'POST':
        db = connect_mysqldb()
        cursor = db.cursor()
        input_name = request.form['input_name']
        input_email = request.form['input_email']
        input_phonenum = request.form['input_phonenum']
        cursor.execute("SELECT * FROM user_info WHERE user_name=%s AND user_email=%s AND user_phonenum=%s ", (input_name, input_email, input_phonenum))
        user_info=cursor.fetchone()
        if user_info:
            user_id = user_info[0]
            return render_template('notice_id.html', user_id=user_id)
        else:
            flash('일치하는 정보 없음')
            return render_template('error_flash.html')
    return render_template('find_id.html')

#아이디 찾기
@app.route('/find_pw', methods=['GET', 'POST'])
def find_pw():
    if request.method == 'POST':
        db = connect_mysqldb()
        cursor = db.cursor()
        input_id = request.form['input_id']
        input_name = request.form['input_name']
        input_email = request.form['input_email']
        input_phonenum = request.form['input_phonenum']
        cursor.execute("SELECT * FROM user_info WHERE user_id=%s AND user_name=%s AND user_email=%s AND user_phonenum=%s ", (input_id, input_name, input_email, input_phonenum))
        user_info=cursor.fetchone()
        if user_info:
            user_pw = user_info[1]
            return render_template('notice_pw.html', user_pw=user_pw)
        else:
            flash('일치하는 정보 없음')
            return render_template('error_flash.html')
    return render_template('find_pw.html')
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')


    
