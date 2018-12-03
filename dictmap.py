#!/usr/bin/python3

import sqlite3

def wordmap(word, db):
    conn = sqlite3.connect(db)
    words = []
    # FIXME: padding, hex checks
    for i in range(0,64,4):
        words.append(word[i:i+4])

    # hex to numbers
    for num in map(lambda x: int(f'0x{x}', 16), words):
        yield lookup_number(conn, num)
    conn.commit()
    conn.close()

def lookup_number(conn, num):
    for row in conn.execute(f'SELECT word FROM words WHERE number = {num}'):
        return row[0]

if __name__ == "__main__":
    print("WORDS: ", end=" ")
    for tw in wordmap("7950f5369c531e869dfac8c9642eba945532715bb638936b8a80b605b2f1090e", "example.db"):
        print(tw, end=" ")
    print("")
