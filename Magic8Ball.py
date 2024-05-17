question = input("Ask me a question ")
import random
answer = random.randint(1,8)
if answer == 1:
    print("it is certain")
elif answer ==2:
    print("Outlook good")
elif answer ==3:
    print("You may rely on it")
elif answer ==4:
    print("Ask again later")
elif answer ==5:
    print("concetrate and ask again")
elif answer ==6:
    print("Reply hazy, try again")
elif answer ==7:
    print("My reply is no")
elif answer ==8:
    print("my source says no")
else:
    print("Thats not a question")
print("the end")