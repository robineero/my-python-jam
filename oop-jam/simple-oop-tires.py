# Python OOP - car tire.

class Tire:

    def __init__(self, brand, model, season, size):
        self.brand = brand
        self.model = model
        self.season = season
        self.size = size  # sellele kohale panen dictionary, et hoida laiust, kõrgust ja diameetrit ühes muutujas.

    def __str__(self):  # see on toString ehk enda loodud objekti kuju, kui seda tüüpi objekti prinditakse
        return f"{self.brand} {self.model} {self.size['width']}/{self.size['height']} {self.size['diameter']}"


def list_of_tires():  # loeb faili ja tagastab Tire tüüpi objekte sisaldava listi.

    tires = []
    with open('simple-oop-tires.csv', mode='r') as file:
        for x in file:
            brand, model, season, width, height, diameter = x.strip().split(",")

            size = {
                "width": int(width),
                "height": int(height),
                "diameter": diameter
            }

            tire = Tire(brand, model, season, size)  # teeb uue Tire tüüpi objekti ja appendib selle listi
            tires.append(tire)

    return tires


def get_tires_by_size(width, height, diameter, catalogue):

    count = 1
    for tire in catalogue:
        if (width == tire.size["width"] and height == tire.size["height"] and diameter == tire.size["diameter"]):
            print(f"{count}. {tire}")
            count += 1


if __name__ == '__main__':
    list_of_tires = list_of_tires()

    print("\nPrindime välja toodete nimekirja: ")
    for tire in list_of_tires:
        print(tire)

    print("\nPrindime valitud parameetritega toodete nimekirja: ")
    get_tires_by_size(205, 55, "R16", list_of_tires)
