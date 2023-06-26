import sys

def main(path):
    # Reading from file from argument
    f = open(path, "r")
    ctx = ""

    for x in f.readline():
        if "small: " in x or "large: " in x:
            t = x.split(" ")
            ctx += " " + t[2] + " '" + t[3].rstrip("\n") + "'\n"
        else:
            ctx += x

    f.close()

    # Writing to file from argument
    f = open(path, "w")
    f.write(ctx)
    f.close()

if __name__ == "__main__":
    main(sys.argv[1])
