import random
import time

saikoukiroku = 999

wait_time = random.randint(5, 15)
time.sleep(wait_time)

start_time = time.time()
print(f"開始時刻:{start_time}") # 開始時刻を表示
print("!!!!!")
input("エンターキーを押してください")

end_time = time.time()
print("終了時刻:{end_time}")
kakatta_byousuu = end_time - start_time
print("かかった時間:{round kakatta_byousuu, 4}秒")
if kakatta_byousuu < 0.01:
    print("不正をしていますね！")

if kakatta_byousuu < saikoukiroku:
    print("新記録です！")
    saikoukiroku = kakatta_byousuu

print("エンターキーが押されました。")

ans = input("もう一度やりますか？(yes/no)")
