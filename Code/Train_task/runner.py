from factories.railcar_factory import RailcarFactory
from factories.cargo_factory import CargoFactory
from train import Train


def main():
    list_of_goods = ["tractor", "tractor", "tractor", "beer", "steel", "steel"]
    train = Train()
    r_factory = RailcarFactory()
    c_factory = CargoFactory()

    for good in list_of_goods:
        new_cargo = c_factory.create(good)
        if new_cargo.name == "tractor":
            railcar = r_factory.create("platform")
            railcar.load_cargo(new_cargo)
            train.add_car(railcar)
        elif new_cargo.name == "beer":
            railcar = r_factory.create("tank")
            railcar.load_cargo(new_cargo)
            train.add_car(railcar)
        elif new_cargo.name == "steel":
            railcar = r_factory.create("container")
            railcar.load_cargo(new_cargo)
            train.add_car(railcar)

    print(train.get_cars())
    print(train.is_able_to_ride())


if __name__ == '__main__':
    main()
