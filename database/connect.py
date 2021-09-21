import psycopg2

conn = psycopg2.connect(
    host="ec2-44-194-225-27.compute-1.amazonaws.com",
    database="d5m0e3fghubm68",
    user="bxzbtbmolqcezz",
    password="1a830ba603fbde5e55dfa39ec5d8b3cc7ee0c5853c5eed27923c1b94983d4533")

conn.set_session(autocommit=True)

connection = conn.cursor()