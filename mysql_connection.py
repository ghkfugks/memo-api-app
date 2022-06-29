import mysql.connector

def get_connection() :
    connection = mysql.connector.connect(
        host = 'yh-db.cx39lhwqkwwy.ap-northeast-2.rds.amazonaws.com',
        database = 'mamo_app_db',
        user = 'memo_user',
        password = 'memo1234',
    )
    return connection