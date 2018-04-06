films = {
    "Finding Dory":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5]
    }
while True:
    choice = input("Hi! What movie would you like to see today?: ").strip().title()
    if choice in films:
        age = int(input("How old are you?: ").strip())
        #check user age
        if age >= films[choice][0]:
            #check enough seats
            num_seats = films[choice][1]
            if num_seats > 0:
                print("Enjoy your movie")
                films[choice][1] = films[choice][1] - 1
            else:
                    print("Oops, we are SOLD OUT")
        else:
            print("Sorry... Our system has established that you're too young to see this movie!")
        
    else:
        print("This movie is NOT availible yet. Please check back at a later time. Thanks")
