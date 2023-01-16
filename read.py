with open("computer_science.txt", "r") as file:
    reading = file.readlines()
for i in range(1, len(reading)):
    listword =reading[i].split()
    for j in range(0, len(listword)):
        print("#"+ listword[j])
   
    print(listword)
    print("@"*100)