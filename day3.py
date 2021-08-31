print("Wellcome to Teasure Island")
print("Your mission is to find the Teasure......")

path = input('Select the path which turn would you like to take "Left" or "Right" ' )
if path == "Left":
    way = input('would you like to "swim" or "wait" ' )
    if way == "wait":
        door = input('which door color would you like to pick "Red" or "Blue" or "yellow" ')
        if door == "yellow":
            print("you win")
        elif door == "Blue":
            print("Eaten by beats....haha....Gameover")    
        elif door== "Red":
            print("Burned by fire....haha...Gameover")    
    elif way == "swim":
        print("Attacked by trout.....Gameover")    
elif path == "Right":
    print("Fall in to hole.....Gameover")            