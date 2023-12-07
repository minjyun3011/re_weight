from db_config import Weight

def display_all_weight():
    for w in Weight.select():
        print(w.id, w.name, w.weight, w.pub_date)

def update_weight(id):
    w = Weight.get_by_id(id)
    w.name = "Sota"
    w.save()

if __name__ == "__main__":
    id = 1
    update_weight(id)


display_all_weight()


