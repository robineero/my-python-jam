# Python OOP.

class Product:

    # Uue toote tegemine tähendab seda, et käivitatakse konstruktor ja luuakse 'andmete komplekt'.
    # Sellest komplektist saab hiljem andmeid küsida. Komplektis olevaid andmeid saab hiljem ka muuta.
    # Konstruktor algab >>
    def __init__(self, brand, model, price, stock, category, tags):
        self.brand = brand
        self.model = model
        self.price = price
        self.stock = stock
        self._volume = 0  # ruumala, _on ees, sest konstruktoris seda pole, vaikimis väärtus, uus väärtus tuleb setterist (kui tuleb)
        self.category = category
        self.tags = tags  # Selle parameetri tüübiks on list

    # << Konstruktor lõppeb

    # See pmst on getter? Näeb välja nagu funktsioon aga tegelikult annab sulle lihtsalt toote infot välja.
    @property  # See on lihtsalt toote üks parameetritest, mis moodustatakse teistest parameetritest.
    def product_name(self):
        return f"{self.brand} {self.model}"

    # Getter ruumala jaoks.
    @property
    def volume(self):
        return self.volume()

    # Setter dekoraator selleks, et muuta erinevatest parameetritest moodustunud parameetrit ühe korraga ?
    # Et muuta parameetrit erilisel viisil?
    # Et muuta privaatseid parameetreid?
    @volume.setter
    def volume(self, volume_string):
        print("Vol string: " + volume_string)
        x, y, z = volume_string.split("x")
        volume = int(x) * int(y) * int(z)
        self._volume = volume


# Siit algab programm. Üleval on lihtsalt funktsionaalsust kirjeldatud.
if __name__ == '__main__':

    # Teen alustuseks kaks toodet (ehk kaks objekti, mille tüübiks on Product (mitte int, string vms))
    # NB! Objekt ei pea tegelikult üldse olema muutujale omistatud! Neid võib niisama ka listi toppida :)
    jalgratas = Product('Valio', 'Speedster Gravel 10', 2299, 1, 'jalgrattad', ['sport', 'scott', 'rattad'])
    parka = Product('Didriksons', 'Dante', 569.95, 10, 'meeste parkad', ['meestele', 'talv'])

    jalgratas.volume = "110x28x82"

    # Nii saan Product tüüpi objektist küsida parameetreid. Näiteks muutujasse 'jalgratas' salvestatud toote brändi.
    print(f"01. Näide, kuidas saab toote andmeid pärida: {jalgratas.brand}")

    # Objektid saan panna ka listi või mistahes kollektsiooni...
    list_of_products = [jalgratas, parka]

    # ... ja seejärjel võtta kõigi listi pandud toodete brändid ja hinnad näiteks nii:
    print("\n02. Meil on olemas järgmised tooted: ")
    for product in list_of_products:
        print(f"{product.product_name} - {product.price} eur")

    print("\n03. Kuna me märkasime, et jalgratta bränd ilmselgelt on vale (Valio), siis paneme rattale õige brändi (Scott): ")
    jalgratas.brand = "Scott"
    print(f"{jalgratas.product_name}  - {product.price} eur")

    print("\n04. Nüüd, kui parandused on tehtud, vaatame, missuguseid tootesilte on kasutatud: ")
    list_of_tags = []

    parka.tags.append("jope")  # lisame ühe tag'i parkale juurde
    jalgratas.tags += ["pro", "2020"]

    for product in list_of_products:  # Käime läbi toodete listi
        for tag in product.tags:  # Iga toote puhul käime läbi parameetri 'tags', mis on omakorda list tootesiltidest
            if tag not in list_of_products:
                list_of_tags.append(tag)
    print(list_of_tags)  # Prindime välja listi, kus on unikaalsed tootesildid.


    # Kuna muutujate nimede väljamõtlemine on pigem tüütu, siis võib tooteid luua ka ilma muutujata :)
    list_of_products = [
        Product('Scott', 'Speedster Gravel 10', 2299, 1, 'jalgrattad', ['sport', 'scott', 'rattad']),
        Product('Asics', 'Gel-Kayano 27', 199, 5, 'jooksujalatsid', ['sport', 'jalatsid', 'mehed', 'nike']),
        Product('Nike', 'Zoom Winflo 7', 114, 8, 'jooksujalatsid', ['sport', 'jalatsid', 'mehed', 'nike'])
    ]

    print("\n05. Teistmoodi tekitatud listis on järgmised tooted: ")

    for product in list_of_products:
        print(f"{product.product_name} - {product.price} eur, (laoseis {product.stock} tk)")

    print("\n06. Küsime listist tooteid, mille bränd on Nike: ")

    for product in list_of_products:
        if (product.brand == "Nike"):
            print(f"{product.product_name} - {product.price} eur, (laoseis {product.stock} tk)")
