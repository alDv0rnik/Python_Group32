from lxml import etree as ET

XML_NS = {"xsi": "http://www.w3.org/2001/XMLSchema-instance"}

root = ET.parse("data/test_ns.xml")
ns = {
    "persons": "http://example.com/persons",
    "olympic": "http://example.com/olympic"
}

for person in root.findall("persons:person", ns):
    name = person.find("persons:name", ns).text
    alias = person.find("olympic:name", ns).text
    field = person.find("olympic:field", ns).text

    print(f"{name}: {alias} -> {field}")

