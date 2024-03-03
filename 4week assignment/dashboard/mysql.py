import pymysql

MYSQL_HOST = 'localhost'
db = pymysql.connect(
    host=MYSQL_HOST,
    port=3306,
    user='root',
    passwd='Itemdogadvantage102!',
    db='dashboard_db',
    charset='utf8'
)

def connect_mysqldb():
    if not db.open:
        db.ping(reconnect=True)
    return db