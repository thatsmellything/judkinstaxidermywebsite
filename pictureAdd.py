import sys, os

#table_file = open('abhi.html', 'w')
#table_file.write('<!DOCTYPE html><html><body>')
#table_file.close()

def cat(args):
    #print("""concatenate files and print on the standard output""")
    for _arg in sys.argv[1:]:
        try:
            with open(_arg, 'r') as _file:
                for _line in iter((_file.readline),""):
                    print (_line, end=" ")
        except IOError as _err:
            sys.stderr.write(os.path.basename(sys.argv[0]) + ": " + _arg +
            ": " + _err.strerror + "\n")

def add(args):
    try:
        with open(sys.argv[1:], 'r') as _file:
            for _line in iter((_file.readline),""):
                print(_line, end=" ")
    except IOError as _err:
            sys.stderr.write(os.path.basename(sys.argv[1]) + ": " + sys.argv[1] +
            ": " + _err.strerror + "\n")

def test():
    with open("file_name.txt", "r") as f:
        lines = f.readlines() 
        lines.remove("Line you want to delete\n")
    with open("new_file.txt", "w") as new_f:
        for line in lines:        
            new_f.write(line)
