from datetime import datetime, timedelta

data = []


while True:
    item = input("項目を追加（exitで終了）:")

    if item == "exit":
        break

    price_input =input("金額を入力（exitで終了）:")
    price = int(price_input)
    if price == "exit":
        break

    
    data.append({
        "date":datetime.now().strftime("%Y-%m-%d"),
        "item":item,
        "price":price})
    print("追加しました")

total = 0
for d in data:
    total += d["price"]

print("今日の家計簿")
for i in data:
    print(f"{d['item']}:{d['price']}円")

print(f"合計金額:{total}円")
