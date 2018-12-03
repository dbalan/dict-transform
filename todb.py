#!/usr/bin/env python3

import sqlite3
import csv

def main(csvfile, db):
    conn = sqlite3.connect(db)
    # Create table
    conn.execute('''CREATE TABLE IF NOT EXISTS words (number integer, word text)''')
    with open(csvfile) as fp:
        words = csv.reader(fp)
        for row in words:
            conn.execute(f'''INSERT INTO words (number, word) VALUES ({int(row[1])}, '{row[2]}')''')
    conn.commit()
    conn.close()
if __name__ == "__main__":
    main("en.csv", "example.db")
