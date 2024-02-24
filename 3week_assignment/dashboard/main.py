from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)


db = pymysql.connect(
    host='localhost',
    user='root',  # MySQL 사용자 이름 입력
    port = 3306,
    password='Itemdogadvantage102!',  # MySQL 비밀번호 입력
    database='dashboard_db',  # 사용할 데이터베이스 이름 입력
    charset='utf8'
)
    


#커서 가져오기
cursor = db.cursor()
create_table_sql = """CREATE TABLE IF NOT EXISTS posts(
    idx INT AUTO_INCREMENT PRIMARY KEY,
    title varchar(20) NOT NULL,
    content varchar(500) NOT NULL
)"""
cursor.execute(create_table_sql)
db.commit()


#처음 화면
@app.route('/')
def index():
    #db에서 게시글들 가져오기
    cursor.execute('SELECT * FROM posts')
    posts = cursor.fetchall()
    return render_template('index.html', posts=posts) #html파일의 posts로 지금 파일의 posts변수 전달

#게시글 조회
@app.route('/<int:idx>')
def view_idx(idx):
    #라우팅 경로에 쓰여진 idx값을 가진 게시물 가져오기
    cursor.execute(f'SELECT * FROM posts WHERE idx={idx}')
    idx_post = cursor.fetchone()
    return render_template('view_idx.html', post=idx_post) 

#게시물 생성
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        cursor.execute("INSERT INTO posts (title, content) VALUES (%s, %s)", (title, content))
        db.commit()
        # 게시물 생성이 끝나면 처음 페이지로 돌아가기
        return redirect('/')
    return render_template('create.html')

#게시물 업데이트
@app.route('/<int:idx>/update', methods=['GET', 'POST'])
def update(idx):
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
    cursor.execute("DELETE FROM posts WHERE idx=%s", idx)
    db.commit()
    return redirect('/')

 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')


    
