from flask_login import UserMixin
from mysql import connect_mysqldb


class User(UserMixin):

    def __init__(self, user_id, user_pw, user_name,user_email, user_phonenum):
        self.id = user_id
        self.pw = user_pw
        self.name = user_name
        self.email = user_email
        self.phonenum = user_phonenum
        

    def get_id(self):
        return str(self.id)

    @staticmethod
    def get(user_id):
        db = connect_mysqldb()
        cursor = db.cursor()
        sql = "SELECT * FROM user_info WHERE USER_ID = '" + str(user_id) + "'"
        cursor.execute(sql)
        user = cursor.fetchone()
        if not user:
            return None

        user = User(user_id=user[0], user_pw=user[1], user_name=user[2], user_email=user[3], user_phonenum=user[4])
        return user

    
