from db_config import Weight

def display_all_weight():
    for w in Weight.select():
        print(w.id, w.name, w.weight, w.pub_date)

def delete_weight(id):
    w = Weight.get_by_id(id)
    w.delete_instance()

if __name__ == "__main__":
    id = 2
    delete_weight(id)
