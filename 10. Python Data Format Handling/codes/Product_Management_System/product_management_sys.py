from add_all_products import add_all_products
from add_new_products import add_new_products
from get_all_products import get_all_products
from get_product_by_id import get_product_by_id
from update_product_by_id import update_product_by_id
from delete_all_products import delete_all_products
from delete_product_by_id import delete_product_by_id

filename = "data.xml"

products = [
    {"id": "1", "name": "Product A", "stock": "100", "price": "1000"},
    {"id": "2", "name": "Product B", "stock": "150", "price": "120"},
    {"id": "3", "name": "Product C", "stock": "200", "price": "800"},
    {"id": "4", "name": "Product D", "stock": "250", "price": "150"},
    {"id": "5", "name": "Product E", "stock": "300", "price": "90"}
]

new_products = [
    {"id": "6", "name": "Product F", "stock": "400", "price": "200"},
    {"id": "7", "name": "Product G", "stock": "500", "price": "250"}
]

updated_product_data = {"id": "3", "name": "Product C", "stock": "555", "price": "800"}

# add_all_products(filename, products)
# get_all_products(filename)
# add_new_products(filename, new_products)
# get_all_products(filename)
# update_product_by_id(filename, 3, updated_product_data)
# get_product_by_id(filename, 3)
# delete_product_by_id(filename, 3)
delete_all_products(filename)

















