
initdict= {"Google":"It is a US based tech company", "TCS":"It is an india based tech company", "Sujeet":"He is a newbie programmer!"}

feedback=input("Type S to search in dictionary.\nType A to add more in dicionary.\n")
feedback.lower()
if feedback=="s":
    search= input("Which word you are looking for?")
    if search not in initdict:
        print("No recoreds found!")
    else:
        print(initdict[search])

elif feedback=="a":
    newWord= input("Enter the new word.\t")
    newDef= input("What do you mean by that new word?\t")
    saveWord= input("Type Y if you are sure to save this new word!")
    saveWord.lower()
    if saveWord=="y":
        initdict.update({newWord:newDef})
        print("New word saved!")
        print(initdict)
    else:
        print("New word is not saved!")            
else:
    print("Try to write S for search and A for adding more words!")   