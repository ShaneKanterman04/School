def exercise1(sentence, word):
    # Find all occurrences of the word within the sentence and store their starting indices in a list.
    print([i for i in range(len(sentence)) if sentence.startswith(word, i)])

def exercise2(list):
    total = 0
    passed6 = 0
    if (len(list) < 0): #print 0 if there are no values in the list
        print('0')
    for i in list: #iterate through each item in list
       if(i == 6):
            passed6 = 1
       elif(passed6 == 0): #added value to total only if the loop didnt pass through a 6 and then a 7
           total += i
       elif(passed6 == 1 and i == 7): # resets the passed6 var to keep adding numbers till the next 6
           passed6 = 0

    print(total)




def main():
    exercise1(input("Enter some text: "),input("Enter a word: "))
    exercise2([1, 2, 2, 6, 99, 99, 7])


main()