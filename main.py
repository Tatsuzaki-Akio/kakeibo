from datetime import datetime, timedelta
import csv

now = datetime.now()

data = []

def del_data():
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

def show_data():
    global data
    for i,d in enumerate(data,1):
        print(f"{i},{d['date']}:{d['item']},{d['price']}")

def write_csv():
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

data = read_csv()
print("既存データを読み込みました")
print("DEBUG: data type =", type(data), " data repr:", repr(data)[:200])



while True:
    item = input("項目を追加（exitで終了）:\n項目を削除（delで項目一覧）:")

    if item == "exit":
        break
    elif item == "del":
        print("家計簿")
        show_data()
        del_data()
        continue

    price_input =input("金額を入力（exitで終了）:")
    if price_input == "exit":
        break
    
    price = int(price_input)


    
    data.append({
        "date":datetime.now().strftime("%Y-%m-%d"),
        "item":item,
        "price":price
        })
    print("追加しました")

write_csv()
print("データを保存しました")


total = 0
for d in data:
    total += int(d["price"])

print(f"今日の家計簿\n{now}\n")
show_data()

print(f"合計金額:{total}円")
