from datetime import datetime, timedelta
import csv

now = datetime.now()

data = []

def del_data(data):
    while True:
        try:
            num = int(input("削除する番号を入力（キャンセルは0）:"))
            if num == 0:
                print("削除をキャンセルしました")
                break

            del data[num - 1]
            print("削除しました")
            break

        except IndexError:
            print("有効な数字を入力してください")
        
        except ValueError:
            print("数字を入力してください")

def show_data(data):
    for i,d in enumerate(data,1):
        print(f"{i},{d['date']}:{d['item']},{d['price']}")

def write_csv(data):
    with open("kakeibo.csv","w",newline="",encoding="utf-8") as f:
        writer = csv.DictWriter(f,fieldnames=["date","item","price"])
        writer.writeheader()
        writer.writerows(data)

def read_csv():
    try:
        with open("kakeibo.csv","r",encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = list(reader)#なんで丸括弧じゃないとエラーが出るのか
            return data
    except FileNotFoundError:
        print("新しい家計簿を作成しました")
        return[]
    
def edit_data(data):
    if not data:
        print("データがありません")
        return
    show_data(data)
    try:
        num = int(input("修正する番号を入力（キャンセルは0）:"))
        if num == 0:
            print("修正をキャンセルしました")
            return
        
        if not (1 <= num <= len(data)):
            print("有効な数字を入力してください")
            return
        
        target = data[num - 1]
        print(f"選択中の項目:{target['date']}|{target['item']}|{target['price']}")

        new_date = input("修正後の日付（空欄なら変更無し）")
        new_item = input("修正後の項目名（空欄なら変更無し）")
        new_price = input("修正後の金額（空欄なら変更無し）")

        if new_date:
            target["date"] = new_date
        if new_item:
            target["item"] = new_item
        if new_price:
            try:
                target["price"] = int(new_price)
            except ValueError:
                print("金額は数字で入力してください")

        data[num - 1] = target
        print("データを修正しました")

    except ValueError:
        print("数字を入力してください")

def add_data(data):
    while True:
        item = input("項目を入力（exitで終了）")
        if item == "exit":
            break

        if not item:
            print("項目は必須です")
            continue

        price_input = input("金額を入力（exitで終了）:")
        if price_input == "exit":
            break

        try:
            price = int(price_input)
        except ValueError:
            print("金額は数字で入力してください")
            continue

    data.append({
        "date":datetime.now().strftime("%Y-%m-%d"),
        "item":item,
        "price":price
        })





data = read_csv()
print("既存データを読み込みました")
# print("DEBUG: data type =", type(data), " data repr:", repr(data)[:200])



while True:
    cmd = input("[コマンド]\n"
                "add:追加|del:削除|edit:修正|exit:終了\n>>")

    if cmd == "exit":
        break

    elif cmd == "del":
        print("家計簿")
        show_data(data)
        del_data(data)
        continue
    
    elif cmd == "edit":
        edit_data(data)

    elif cmd == "add":
        add_data(data)
        print("追加しました")
        write_csv(data)

    else:
        print("無効なコマンドです")


total = 0
for d in data:
    total += int(d["price"])

print(f"今日の家計簿\n{now}\n")
show_data(data)

print(f"合計金額:{total}円")
