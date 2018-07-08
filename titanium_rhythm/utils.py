from os.path import splitext

def get_file_type(filepath):
    return splitext(filepath)[1][1:]