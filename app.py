from db_config import Weight

def delete_weight():
    w_name = input("体重を削除するユーザーを入力してください > ")
    w = Weight.get(w_name)
    if not w.delete_instance():
        print("削除に失敗しました。")

def create_weight():
    name = input("名前を入力してください > ")
    weight = input("体重を入力してください > ")

    try:
        w = Weight.get(name=name)
        # 同じ名前が存在する場合は更新処理を行う
        w.weight = weight
        w.save()
        print("更新に成功しました。")
    except Weight.DoesNotExist:
        # 同じ名前が存在しない場合は新規作成
        w = Weight.create(name=name, weight=weight)
        print("新しい体重データを作成しました。")

def show_weight():
    for w in Weight.select():
        print(f"{w.id} {w.name} {w.weight} {w.pub_date}")

def main():

    while True:
        msgs = input("データの入力(\c)・表示(\s)・終了(\q)を選択してください > ")

        if msgs == "\c":    
            create_weight()
            continue

        if msgs == "\s":    
            show_weight()    
            continue

        if msgs == "\q":    
            break
    
        if msgs == "\d":    
            delete_weight()    
            continue
        



if __name__ == "__main__":
    main()

