print("Welcome to my computer quiz!")

playing = input("Do u want to play? ")

if playing.lower() != "yes":
    quit()

print ("okay! Let's play :)")

score = 0

answer = input("How many continents are there? ")
if answer.lower() == "7":
    print('Correct! ')
    score += 1 
else:
    print("Incorrect!")
answer = input(" What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct! ')
    score +=  1
else:
    print("Incorrect!")
answer = input(" how many hours are there in a day? ")
if answer.lower() == "24":
    print('Correct! ')
    score += 1 
else:
    print("Incorrect!")
answer = input(" what does RAM mean? ")
if answer.lower() == "Random access memory":
    print('Correct! ')
    score += 1 
else:
    print("Incorrect!")
print ("You got " + str(score) + " questions correct! ")
