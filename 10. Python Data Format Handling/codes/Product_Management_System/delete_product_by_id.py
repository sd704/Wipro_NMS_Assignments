import xml.etree.ElementTree as ET


def delete_product_by_id(filename, product_id):
    tree = ET.parse(filename)
    root = tree.getroot()

    for product in root.findall("product"):
        id = product.find("id").text
        if id == str(product_id):
            root.remove(product)
            tree.write(filename)
            print(f"Product with id {product_id} deleted successfully.")
            return True

    print(f"Product with ID {product_id} not found!")
    return False
