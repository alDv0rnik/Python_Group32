from xml.etree import ElementTree as ET

root = ET.parse("data/data.xml")
items = root.findall("./items/item")

print(list(map(lambda x: x.text, items)))