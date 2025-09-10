import random

print("=== ヒットアンドブロー ===")

# 最短記録
best_score = None

while True:
    # 難易度（桁数）を選ぶ
    digits = int(input("桁数を選んでください（3〜6）："))
    while digits < 3 or digits > 6:
        digits = int(input("もう一度、3〜6の数字で選んでください："))

    # 答えを作る（数字がすべて違う）
    numbers = list("0123456789")
    random.shuffle(numbers)
    answer = ""
    for i in range(digits):
        answer += numbers[i]

    # 回数カウントとヒントの使用
    count = 0
    hint_used = False

    print("\n数字を当ててください！（すべて違う数字）")
    print("hint と入力するとヒントが出ます（1回だけ！）")
    print("exit と入力するとゲームをやめます")

    while True:
        guess = input(f"{count + 1}回目の予想：")

        if guess == "exit":
            print("ゲームをやめました。")
            exit()

        if guess == "hint":
            if not hint_used:
                print("ヒント：答えに「" + answer[0] + "」が含まれています")
                hint_used = True
            else:
                print("ヒントはもう使いました。")
            continue

        # チェック（数字だけ・桁数・バラバラの数字）
        if len(guess) != digits:
            print(f"{digits}桁の数字を入力してください。")
            continue
        if not guess.isdigit():
            print("数字だけで入力してください。")
            continue
        if len(set(guess)) != digits:
            print("同じ数字は使えません。")
            continue

        # 回数＋1
        count += 1

        # ヒット・ブロー数を数える
        hit = 0
        blow = 0
        for i in range(digits):
            if guess[i] == answer[i]:
                hit += 1
            elif guess[i] in answer:
                blow += 1

        print(f"{hit} Hit / {blow} Blow")

        if hit == digits:
            print("正解！！！👏✨✨", count, "回目でクリア！")
            if best_score is None or count < best_score:
                best_score = count
                print("新記録！")
            else:
                print("今までの最短記録：", best_score, "回")
            again = input("もう一度やりますか？（Yes / No）：")
            if again.lower() == "yes":
                break  # 最初から
            else:
                print("またね！")
                exit()
