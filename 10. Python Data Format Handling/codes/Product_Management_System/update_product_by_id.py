import xml.etree.ElementTree as ET


def update_product_by_id(filename, product_id, updated_data):
    tree = ET.parse(filename)
    root = tree.getroot()

    for product in root.findall("product"):
        id = product.find("id").text
        if id == str(product_id):
            for key, value in updated_data.items():
                product.find(key).text = value
            tree.write(filename)
            print(f"Product with id {product_id} updated successfully.")
            return True

    return False
