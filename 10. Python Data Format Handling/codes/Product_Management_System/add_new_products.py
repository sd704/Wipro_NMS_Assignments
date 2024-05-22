import xml.etree.ElementTree as ET
import os
from add_all_products import add_all_products


def add_new_products(filename, new_products):
    if not os.path.exists(filename):
        print(f"File {filename} does not exist. Creating a new file.")
        add_all_products(filename, new_products)
        return

    tree = ET.parse(filename)
    root = tree.getroot()

    for product in new_products:
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

    tree.write(filename)
