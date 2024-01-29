from xml.etree import ElementTree as ET
import json

# filepath = "data/data.xml"
# root = ET.parse(filepath)
# print(root)
# elements = root.findall("items")
# element = root.find("items")
# print(element)
#
# for elem in element:
#     print(elem.attrib, end=" ")  # Получаем словарь атрибутов
#     print(elem.text)  # Выводит значения тэгов


# filepath = "data/animals.xml"
# root = ET.parse(filepath)
# elements = root.findall("animal")
#
#
# def parse_elements(elem: ET) -> dict:
#     animal = {
#         "id": str(elem.attrib.get("id")),
#         "type": elem.find("type").text,
#         "owner": elem.find("owner").text
#     }
#     return animal
#
#
# animals = [parse_elements(element) for element in elements]
# print(animals)
#
# with open("data/animals.json", "w") as file:
#     json.dump(animals, file)


#### WRITE XML ####

#
# root = ET.Element("numbers")
#
# for i, n in enumerate(range(1, 4), start=1):
#     element = ET.SubElement(root, "number")
#     element.attrib = dict(id=str(i))
#     element.text = str(n * 10)
#
# print(ET.dump(root))
# tree = ET.ElementTree(root)
# tree.write("data/output.xml")


persons = [
    {"id": 1, "name": "John", "surname": "Connor", "age": 15},
    {"id": 2, "name": "Sarah", "surname": "Connor", "age": 33},
    {"id": 3, "name": "Arnold", "surname": "T-800", "age": 45}
]

root = ET.Element("persons")

for person in persons:
    elem = ET.SubElement(root, "person", attrib=dict(id=str(person["id"])))
    name = ET.SubElement(elem, "name", attrib=dict(lang="eng"))
    surname = ET.SubElement(elem, "surname", attrib=dict(lang="eng"))
    age = ET.SubElement(elem, "age")
    name.text = person.get("name")
    surname.text = person.get("surname")
    age.text = str(person.get("age"))

tree = ET.ElementTree(root)
tree.write("data/persons.xml")