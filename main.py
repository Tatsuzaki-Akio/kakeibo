from datetime import datetime, timedelta
import csv

now = datetime.now()

data = []

try:
    with open("kakeibo.csv","r",encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)
    print("既存データを読み込みました")
except FileNotFoundError:
    print("新しい家計簿を作成します")



while True:
    item = input("項目を追加（exitで終了）:")

    if item == "exit":
        break

    price_input =input("金額を入力（exitで終了）:")
    if price == "exit":
        break
    price = int(price_input)


    
    data.append({
        "date":datetime.now().strftime("%Y-%m-%d"),
        "item":item,
        "price":price
        })
    print("追加しました")

with open("kakeibo.csv","w",newline = "",encoding="utf-8") as f:
    writer = csv.DictWriter(f,fieldnames=["date","item","price"])
    writer.writeheader()
    writer.writerows(data)

print("データを保存しました")


total = 0
for d in data:
    total += int(d["price"])

print(f"今日の家計簿\n{now}\n")
for i ,d in enumerate(data,1):
    print(f"{i}.{d['item']}:{d['price']}円")

print(f"合計金額:{total}円")
