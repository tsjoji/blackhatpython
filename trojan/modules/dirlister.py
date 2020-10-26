import os
def run(**args):
    print("[*] In dilister module.")
    files = os.listdir(".")
    return str(files)
