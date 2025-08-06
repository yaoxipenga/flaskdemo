import sqlite3
from datetime import datetime
from zoneinfo import ZoneInfo

now = datetime.now(ZoneInfo("Asia/Shanghai")).strftime("%Y-%m-%d %H:%M:%S")

conn = sqlite3.connect('database.db')

with open('db.sql', 'r', encoding='utf-8') as f:
    conn.executescript(f.read())

cur = conn.cursor()
cur.execute("INSERT INTO posts (title, content, created) VALUES (?, ?, ?)", ('flask1', '学习1', now))
cur.execute("INSERT INTO posts (title, content, created) VALUES (?, ?, ?)", ('flask2', '学习2', now))

conn.commit()
conn.close()

