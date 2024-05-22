import xml.etree.ElementTree as ET


def get_product_by_id(filename, product_id):
    tree = ET.parse(filename)
    root = tree.getroot()
    found = False

    for product in root.findall("product"):
        id = product.find("id").text
        if id == str(product_id):
            found = True
            name = product.find("name").text
            stock = product.find("stock").text
            price = product.find("price").text
            print(f"ID: {id}, Name: {name}, Stock: {stock}, Price: {price}")
            break

    if not found:
        print(f"Product with ID {product_id} not found!")
