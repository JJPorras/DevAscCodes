def legal_ages():
    lifeEvent = (16, 18, 21, 65)
    print("Drive: " + str(lifeEvent[0]))
    print("Voting: " + str(lifeEvent[1]))
    print("Drinking: " + str(lifeEvent[2]))
    print("Retirement: " + str(lifeEvent[3]))

print("Now with a Dictionary")

def legal_ages2():
    lifeEvent2 = {
    "Drive" : 16,
    "Voting" : 18,
    "Drinking" :21,
    "Retirement" : 65
    }
    print("Drive: " + str(lifeEvent2["Drive"]))
    print("Voting: " + str(lifeEvent2["Voting"]))
    print("Drinking: " + str(lifeEvent2["Drinking"]))
    print("Retirement: " + str(lifeEvent2["Retirement"]))

#legal_ages()
#legal_ages2()

for i in range(5):
    print(i)

list = ["hola", "como", "estas", 2, 1]

for i in list:
    print(i)

dictionary = {"perro":1, "gato":2}

for i in dictionary:
    print(i)

dictionary = {"perro":1, "gato":2}

for i in dictionary.items():
    print(i)
