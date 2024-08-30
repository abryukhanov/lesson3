from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Samsung", "Galaxy S20 Ultra", "+79223456789"))
catalog.append(Smartphone("Apple", "iPhone 13 Pro Max", "+79133456780"))
catalog.append(Smartphone("Xiaomi", "Mi 11 Ultra", "+79533456781"))
catalog.append(Smartphone("Huawei", "Nova 5T", "+79133456782"))
catalog.append(Smartphone("OnePlus", "10t", "+79833456783"))

for smartphone in catalog:
    print(smartphone)