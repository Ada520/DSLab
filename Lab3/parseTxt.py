import os
def parseTxt():
    directory = "C:/Users/kevjy/Documents/Fall2017/EE379K/Labs/DSLab/Lab3/scrapedTXT/"
    outfile = open('concatTXT.txt', "r+")
    for x in os.listdir(directory):
        fname = os.path.join(directory, x)
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

    outfile.close()


if __name__ == "__main__":
    parseTxt()