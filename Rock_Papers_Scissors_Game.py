from random import randint

def game(computer,human,hScore,cScore,draw):
    
    if computer == human:
        draw += 1
    elif computer==1:
        if human==2:
            hScore += 1
        elif human==3:
            cScore += 1
    elif computer==2:
        if human==3:
            hScore += 1
        elif human==1:
            cScore += 1
    elif computer==3:
        if human==1:
            hScore += 1
        elif human==2:
            cScore += 1
    
    return hScore,cScore,draw

hScore = 0
cScore = 0
draw = 0
count = 0

while count <10:

    computer = randint(1,3)
    print("\n\nSelect your option as following.\n1 --> rock \n2 --> Paper \n3 --> Scissors ")
    
    optionsList = [1,2,3]
    try:
        human = int(input("Enter your option: "))
    except ValueError:
        print("\n\tEnter valid option\n")
        continue
    if human in optionsList:
        print(f"computer' option: {computer} and your's option = {human}")
        hScore,cScore,draw=game(computer,human,hScore,cScore, draw)
    else:
        print("\n\tEnter valid option\n")
        continue
     
    count += 1
    print(count)

print(f"Draw = {draw}")
print(f"computer Score: {cScore} and your's Score = {hScore}")






