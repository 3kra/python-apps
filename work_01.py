# input_line = input("何か入れて：")
# print(input_line)

import random

import mysql.connector

# MySQLサーバーへの接続情報
conn = mysql.connector.connect(
    host="localhost", user="root", password="dyufr4hd63hrd", database="my_db"
)
# mysqlに接続 データベース名分からなければ show databases;で確認

if conn.is_connected():
    print("MySQLサーバーに接続成功！")


cur = conn.cursor()

while True:

    answer = random.randint(1, 100)
    print(answer)

    result = False
    cnt = 0
    for i in range(5):
        cnt = cnt + 1
        input_line = int(input("1〜100までの数字を入力してください："))
        # 入力された文字があってたら→「当たり！」、外れてたら→「不正解」を表示
        if input_line == answer:
            print("正解です！")
            result = True
            break
        else:
            print("不正解です!")
            # ヒントを出す
            if input_line < answer:
                print("もっと大きい数字です")

                # どのくらい大きいか教える
                if answer - input_line > 10:
                    print("10以上大きいです")
                else:
                    print("もっと大きい数字ですが、だいぶ近いです")
            else:
                if input_line - answer > 10:
                    print("10以上小さいです")
                else:
                    print("もっと小さいですが、だいぶ近いです")

    # もう一度チャレンジするかきく

    if result:
        print(f"ゲームに勝ちました。あなたは{cnt}回目で正解しました。")
        cursor = conn.cursor()

        # データ挿入のクエリ
        insert_query = "INSERT INTO users (username, email) VALUES (%s, %s)"
        data = ("user1", "user1@example.com")

        # クエリ実行
        cursor.execute(insert_query, data)

        # 変更を反映
        conn.commit()
    else:
        print(f"ゲームに負けました。正解は{answer}でした。")

    ans = input("もう一度やりますか？（yes/no):")

    if ans == "yes":
        continue
    else:
        print("さようなら")
        break
