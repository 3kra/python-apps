import mysql.connector

# MySQLサーバーに接続
conn = mysql.connector.connect(
    host="localhost", user="root", password="あなたのパスワード"
)

cur = conn.cursor()

# データベース作成
cur.execute("CREATE DATABASE IF NOT EXISTS app_records")

print("データベース app_records を作成しました！")

conn.close()
