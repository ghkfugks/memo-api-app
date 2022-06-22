import mysql.connector

def get_connection() :
    connection = mysql.connector.connect(
        host = 'yh-db.cx39lhwqkwwy.ap-northeast-2.rds.amazonaws.com',
        database = 'mamojog_db',
        user = 'mamo_user',
        password = 'mamo1234',
    )
    return connection