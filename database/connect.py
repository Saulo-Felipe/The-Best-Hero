import psycopg2

conn = psycopg2.connect(
    host="batyr.db.elephantsql.com",
    database="niiaxvpj",
    user="niiaxvpj",
    password="CSdaMAAEhIWN_VYLHoeeGyiIDo_6x-R2")

connection = conn.cursor()

'''
connection.execute("SELECT * FROM clients")

records = connection.fetchall()

'''