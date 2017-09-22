import os
def parseTxt():
    directory = "C:/Users/kevjy/Documents/Fall2017/EE379K/Labs/DSLab/Lab3/scrapedTXT/"
    outfile = open('train.txt', "r+")
    for x in os.listdir(directory):
        fname = os.path.join(directory, x)
        if os.path.isfile(fname):
            with open(fname) as f:
                wordList = f.read().split()
                for word in wordList:
                    if word.isalpha():
                        outfile.write(word + " ")

    outfile.close()


if __name__ == "__main__":
    parseTxt()