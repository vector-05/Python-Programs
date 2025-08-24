import random
user = input("Play | ")
aicount = 0
uscount = 0
p1 = "Stone"
p2 = "Paper"
p3 = "Scissor"
while uscount < 5 or aicount < 5:
        usch = input("Your Turn | ")
        i = random.choice([p1,p2,p3])
        print("Player Turn | ",i)
        if usch == i:
            aicount = aicount
            uscount = uscount
            print("| Chance Draw |")
            print("Your Points | ",uscount)
            print("AI Points | ",aicount)
        elif usch == p1 and i == p2:
            aicount = aicount + 1
            uscount = uscount
            print("| AI got you |")
            print("Your Points | ",uscount)
            print("AI Points | ",aicount)
        elif usch == p1 and i == p3:
            aicount = aicount
            uscount = uscount + 1
            print("| You got AI |")
            print("Your Points | ",uscount)
            print("AI Points | ",aicount)
        elif usch == p2 and i == p1:
            aicount = aicount
            uscount = uscount + 1
            print("| You got AI |")
            print("Your Points | ",uscount)
            print("AI Points | ",aicount)
        elif usch == p2 and i == p3:
            aicount = aicount + 1
            uscount = uscount
            print("| AI got you |")
            print("Your Points | ",uscount)
            print("AI Points | ",aicount)
        elif usch == p3 and i == p1:
            aicount = aicount + 1
            uscount = uscount
            print("| AI got you |")
            print("Your Points | ",uscount)
            print("AI Points | ",aicount)
        elif usch == p3 and i == p2:
            aicount = aicount
            uscount = uscount + 1
            print("| You got AI |")
            print("Your Points | ",uscount)
            print("AI Points | ",aicount)
else:
    print("Game Over")
