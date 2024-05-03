
# Description: English to Hmong Translator

x = ""
dictionary = {}
def main():
    load_dictionary('HmongWords.txt')
    while True:
        sentence = ""
        inp = str(input("Type your English Sentence: "))
        kale = inp.split()
        for i in kale:
            i = i.replace(',', '').replace("'", "").replace('.', "").replace("!", '').replace(':', '').replace("?", '')
            i = i.lower()
            i.split(" ")
            sentence += translate(i) + " "
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
        print(sentence)
        while True:
            inp2 = input("Another translation (Y/N): ")
            if inp2 == "y" or inp2 == "Y":
                break
            elif inp2 == "n" or inp2 == "N":
                print_word_frequency(dictionary)
                return
            else:
                print("Please try again enter Y or N.")
def load_dictionary(filename):
    global eng2hmong
    eng2hmong = {}
    global x
    x = open(filename, 'r')
    for line in x:
        idk = line.split(",")
        idk[2] = idk[2].replace("\n", "")
        eng2hmong[idk[2]] = idk[1]
        eng2hmong.update()

def translate(i):
    if i in eng2hmong:
        trans_word = eng2hmong[i]
        return trans_word
    else:
        trans_word = "?"
        return trans_word
def print_word_frequency(dictionary):
    print("Word Frequency")
    print("____________________________")
    for key, value in dictionary.items():
        print(key, ":", value)

if __name__ == "__main__":
    main()
