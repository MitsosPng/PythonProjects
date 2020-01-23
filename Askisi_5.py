
def bigger_than_3_words (filename):
    with open(filename, 'r') as infile:
        words=infile.read().split()
    for word in words:
        if len(word)>3:
            first=word[0]
            new_word = "" + word[1:]
            new_word = new_word+first+"ay"
            print (new_word)

bigger_than_3_words('mp.txt')