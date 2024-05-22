import os


def delete_all_products(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"File {filename} deleted successfully!")
    else:
        print(f"No such file {filename}")
