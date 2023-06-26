from util import util as f2

def print_test(txt:str):
    print("*** running in file1.py ")
    f2.print_test(txt)

if __name__ == '__main__':
    print_test("hello")
