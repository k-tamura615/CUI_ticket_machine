import os
def clear_screen():  # 画面クリア
    os.system('cls' if os.name == 'nt' else 'clear')
def main():  # スタート画面
    while True:
        clear_screen()
        print("***********************")
        print("\n 券売機シミュレータ\n")
        print("***********************\n")
        print("Please Enter (Enterキーを押して商品選択）")
        print("       （aキーを押して管理画面）")
        print("       （qキーを押して終了）\n")
        user_input = input()
        if user_input.lower() == 'q':
            break
        elif user_input.lower() == 'a':
            admin_screen()
        else:
            vending_machine()
items = {
    1: {"name": "味噌カレー牛乳ラーメン（バター入り）", "price": 980, "sold": 0},
    2: {"name": "味噌牛乳ラーメン（バター入り）", "price": 980, "sold": 0},
    3: {"name": "牛乳ラーメン（バター入り）【塩】", "price": 980, "sold": 0},
    4: {"name": "中華そば【煮干し醬油】", "price": 600, "sold": 0}
}
sales_reset = False
def vending_machine():  # 利用者画面
    cart = {}
    while True:
        clear_screen()
        print("商品      金額")
        print("=======================")
        for key, value in items.items():
            print(f"{key}.{value['name']} {value['price']}円")
        print("\n購入する商品番号(支払いに進む場合はc)>", end="")
        choice = input().strip()
        if choice == 'c':
            checkout(cart)
            break
        elif choice.isdigit() and int(choice) in items:
            item_number = int(choice)
            cart[item_number] = cart.get(item_number, 0) + 1
        else:
            print("無効な入力です。もう一度入力してください。")
            input("Enterキーを押して続ける...")
def checkout(cart):  # 支払い画面
    if not cart:
        print("カートに商品がありません。")
        input("Enterキーを押して戻る...")
        return
    total = sum(items[item]['price'] * quantity for item, quantity in cart.items())
    print("\n商品       数量")
    for item, quantity in cart.items():
        print(f"{items[item]['name']}   {quantity}")
        items[item]['sold'] += quantity
    print("===")
    print(f"\n合計{total}円")
    while True:
        print("\n現金を投入してください>", end="")
        cash = input().strip()
        if cash.isdigit() and int(cash) >= total:
            change = int(cash) - total
            print(f"\nご購入ありがとうございます。おつり{change}円です。")
            input("Enterキー押下でタイトル画面の表示に戻る")
            break
        else:
            print("金額が不足しています。正しい金額を投入してください。")
def admin_screen():  # 管理者画面
    global sales_reset
    while True:
        clear_screen()
        print("\n======= 商品一覧 =======")
        print("\n商品      単価  販売数  売上金額")
        print("=======================")
        total_sales = 0
        for key, value in items.items():
            sales = value['price'] * value['sold']
            total_sales += sales
            print(f"{key}.{value['name']} {value['price']}円  {value['sold']}   {sales}円")
        print("\n———")
        print(f"総売上金額 {total_sales}円\n")
        print("=== 管理メニュー ====")
        print("1. 売上をリセットする")
        print("2. 商品の価格を変更する（売上リセット後のみ可能）")
        print("3. 管理画面を終了する")
        choice = input("管理メニューを選択してください>").strip()
        if choice == '1':
            for item in items.values():
                item['sold'] = 0
            sales_reset = True
            print("売上をリセットしました。")
            input("Enterキーを押して戻る...")
        elif choice == '2':
            if sales_reset:
                change_price()
            else:
                print("売上をリセットしてから価格を変更してください。")
                input("Enterキーを押して戻る...")
        elif choice == '3':
            break
        else:
            print("無効な入力です。")
            input("Enterキーを押して続ける...")
def change_price():  # 価格変更画面
    print("\n価格を変更する商品の番号を入力してください。")
    choice = input().strip()
    if choice.isdigit() and int(choice) in items:
        item_number = int(choice)
        print(f"現在の価格: {items[item_number]['price']}円")
        new_price = input("新しい価格を入力してください>").strip()
        if new_price.isdigit():
            items[item_number]['price'] = int(new_price)
            print(f"{items[item_number]['name']} の価格を {new_price}円 に変更しました。")
        else:
            print("無効な入力です。数値を入力してください。")
    else:
        print("無効な入力です。")
    input("Enterキーを押して戻る...")
if __name__ == "__main__":
    main()