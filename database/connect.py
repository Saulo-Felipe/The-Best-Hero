import psycopg2

conn = psycopg2.connect(
    host="db.iiyunbxnpsorezcvitbs.supabase.co",
    database="postgres",
    user="postgres",
    password="the-best-hero")

conn.set_session(autocommit=True)

connection = conn.cursor()