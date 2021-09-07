import psycopg2

conn = psycopg2.connect(
    host="chunee.db.elephantsql.com",
    database="rlajypdt",
    user="rlajypdt",
    password="0XXi13pbmWolYn47_U6WBiqumBL9ZbIe")

conn.set_session(autocommit=True)

connection = conn.cursor()