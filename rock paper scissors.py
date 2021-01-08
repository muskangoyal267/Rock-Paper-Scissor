array = ["rock", "scissor", "paper"]
player_1 = input("Player-1, Enter your name: ")
player_2 = input("Player-2, Enter your name: ")

def game():
    while True:
            shoot_1 , shoot_2 = input(player_1 + " and " + player_2 + " shoot-- ").lower().split(',')
            if shoot_1 and shoot_2 in array:
                if shoot_1 == shoot_2:
                    print("It's a tie!, trial not counted")
                    continue
                elif shoot_1 in array[0] and shoot_2 in array[1]:
                    print("Congratulations! " + player_1 + " , You won!" +"\n"+ player_2 + " Better luck next time. ")
                    break
                elif shoot_1 in array[1] and shoot_2 in array[2]:
                    print("Congratulations! " + player_1 + " , You won!" + "\n" + player_2 + " Better luck next time. ")
                    break
                elif shoot_1 in array[2] and shoot_2 in array[0]:
                    print("Congratulations! " + player_1 + " , You won!" + "\n" + player_2 + " Better luck next time. ")
                    break

                else:
                    print("Congratulations!" + player_2 + " , You won! " + "\n" + player_1 + " Better luck next time. ")
                    break


            else:
                print("Bsdk, Dimag lga kr shoot kr.")
                continue
game()
count = 1
limit = 3
while True:
    if count<limit:
         note =input("Do you want to play again? ")
         array_1 = ["yes","y","Y","Yes"]
         if note in array_1:
             game()
             count += 1
         else:
            print("Thank You!")
            count = 1
            break
    else:
        print("You are out of moves")

