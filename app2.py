from db_config import Weight

def display_all_weights():
    for w in Weight.select():
        print(w.id, w.name, w.weight, w.pub_date)

if __name__ == "__main__":
    display_all_weights()

