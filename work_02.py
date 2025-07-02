# work_02 反射神経テスト

# プログラムが5〜15秒の間でランダムな時間待機した後合図を出す
import random
import time

while True:

    records = []
    # 5〜15秒の間でランダムな時間を決める
    wait_time = random.randint(5, 15)

    # 指定時間だけ待機する
    time.sleep(wait_time)

    # 合図を出す
    print("！！！！！")
    input("エンターキーを押してください:")

    # 合図が出てからエンターが押されるまでの時間を計る
    start_time = time.time()

    input()

    end_time = time.time()

    jikann = end_time - start_time

    # 記録を保存
    records.append(jikann)

    # 反応時間を小数点以下4桁
    print(f"{jikann:.4f}秒")

    # 連打などへの対策として、反応速度が0.01秒未満で押されていた場合は不正とする
    if jikann <= 0.01:
        print("不正をしていますね!!")
    else:
        print()

    # もう一回チャレンジするか聞いて、返事を入力させ、再チャレンジできるようにする
    ans = input("もう一度やりますか？（yes/no):")

    if ans.lower() == "yes":
        continue
    else:
        #  さようならの前にこれまでの最高記録を表示する
        saisoku = min(records)
        print(f"これまでの最高記録は{saisoku:.4f}秒でした")
        print("さようなら")
        break