word = input("Please ENter your own word")
char = input("Pleae enter the chracater")
i = 0 
count = 0
#loop to find the occurence of character
while(i < len(word)):
    if (word [i] == char):
        count = count + 1
    i = i + 1
print("total number of times", char , "has occured = ", count)