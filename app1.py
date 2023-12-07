from db_config import Weight

def create_weight():
    weight = Weight(name="So", weight=60)
    weight.save()

    Weight.create(name="Ryu", weight=62)

if __name__ == "__main__":
    create_weight()
