import xml.etree.ElementTree as ET


def get_all_products(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    for product in root.findall("product"):
        id = product.find("id").text
        name = product.find("name").text
        stock = product.find("stock").text
        price = product.find("price").text
        print(f"ID: {id}, Name: {name}, Stock: {stock}, Price: {price}")
