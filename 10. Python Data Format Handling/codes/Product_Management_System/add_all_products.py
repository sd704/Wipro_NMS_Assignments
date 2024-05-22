import xml.etree.ElementTree as ET


def add_all_products(filename, product_data):
    root = ET.Element("data")

    for product in product_data:
        product_element = ET.SubElement(root, "product")

        id_element = ET.SubElement(product_element, "id")
        id_element.text = product["id"]

        name_element = ET.SubElement(product_element, "name")
        name_element.text = product["name"]

        stock_element = ET.SubElement(product_element, "stock")
        stock_element.text = product["stock"]

        price_element = ET.SubElement(product_element, "price")
        price_element.text = product["price"]

        print(f"Product with ID {product["id"]} added.")

    tree = ET.ElementTree(root)
    tree.write(filename)
