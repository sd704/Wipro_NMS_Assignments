import os


def delete_json(file):
    if os.path.exists(file):
        os.remove(file)
        print(f"File {file} deleted successfully!")
    else:
        print(f"No such file {file}")
