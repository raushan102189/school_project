with open("computer_science.txt", "r") as file:
    reading = file.readlines()
lowercase =0
uppercase =0
vowel_count =0
consonent_count =0

vowel = ["a", "e", "i", "o", "u"]
consonent = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

for i in range(1, len(reading)):
    listword =reading[i].split()
    for j in range(0, len(listword)):
        for k in range(0, len(listword[j])):
            listletter = listword[j][k]
            if listletter.islower():
                lowercase +=1
            elif listletter.isupper():
                uppercase +=1
            if listletter.lower() in vowel:
                vowel_count +=1
            
            elif listletter.lower() in consonent:
                consonent_count +=1
print("lowercase: ", lowercase)
print("uppercase: ", uppercase)
print("vowel_count: ", vowel_count)
print("consonent_count: ", consonent_count)
print("total: ", lowercase+uppercase)