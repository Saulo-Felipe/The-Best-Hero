import pygame 
import os
from root import connection

def rankingScreen(screen):
    connection.execute('SELECT * FROM clients')

    records = connection.fetchall()
    
    print(records)

