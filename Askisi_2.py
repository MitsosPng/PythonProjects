
def good_bad_words(filename):

    with open(filename, 'r') as infile:
        words=infile.read().split()
    letters=["f","F","c","C","k","K","r","R"]
    for word in words :
            count_bad=0
            count_good=0
            for i in word :
                if i in letters :
                    count_bad+=1
                else:
                    count_good+=1
            if count_bad>=count_good:
                print("Bad Word")
            else:
                print("Good Word")
good_bad_words('mp.txt')