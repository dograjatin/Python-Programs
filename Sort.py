def sentence_sort(sentence):
    list = sorted(sentence.lower().split())
    out = " ".join(map(str,list))
    print(out)

def string_sort(sentence):
    list = sorted(sentence.lower())
    out = " ".join(map(str,list)).replace(" ","")
    print(out)

sentence = input("Please Enter a sentence\n")

print('''Please choose an option for sorting
            Choose 1 to Sort Words 
            Choose 2 to Sort Alphabets''')
while True:
    option = input()
    if option == '1':
        sentence_sort(sentence)
    elif option == '2':
        string_sort(sentence)
    elif option is '':
        break
    else:
        print("Please choose correct option")

