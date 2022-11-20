import psycopg2

conn = psycopg2.connect(
    host="babar.db.elephantsql.com",
    database="gdbhfzwz",
    user="gdbhfzwz",
    password="Lb4-wkTyUVoTCnES3syU2TF49x9Cg2cJ")

conn.set_session(autocommit=True)

connection = conn.cursor()