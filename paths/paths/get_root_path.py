from os.path import dirname

def root_path():
    return dirname(dirname(dirname(__file__)))



if __name__ ==  "__main__":
    print(root_path())