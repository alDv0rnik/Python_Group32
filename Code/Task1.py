"""
Используя ElementTree выполнить парсинг xml файла следующего содержания

<data>
    <items>
        <item name="item1">10</item>
        <item name="item2">20</item>
        <item name="item3">30</item>
        <item name="item4">40</item>
    </items>
</data>

На выходе программы должны получить список {'attrib': 'value'}.
Сохраните полученный список в json формате

"""
import json
from xml.etree import ElementTree as ET


root = ET.parse("data/books.xml")
elements = root.findall("book")
books = []

for element in elements:
    books.append(
        {"category": element.attrib.get("category")}
    )

with open("data/books.json", "w") as file:
    json.dump(books, file)