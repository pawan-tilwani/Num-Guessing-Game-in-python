import random
num = random.randint(1, 100);
attempt = 10

while True:
    user = int(input("Enter your guessing : "))
    if user == num:
        print(f"You Win ! The Number Was {num}")
        break
    else:
        if user < num:
            print("Number is Too Low !\n Try Again ")
            attempt = attempt - 1
            print(f"Attempt Left = {attempt}")
        elif user > num:
            print("Number is Too High !\n Try Again ")
            attempt = attempt - 1
            print(f"Attempts Left = {attempt}")
    if attempt == 0:
        print("You Loose ! , No attempts are left")
        break        
            

