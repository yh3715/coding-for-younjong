
import random

rock = "바위"
scissors = "가위"
paper = "보"


list_a = (rock, scissors, paper)


win_score = 0
lose_score = 0

while win_score < 2 and lose_score < 2:

    user_choice = input("{}, {}, {} 중 무엇을 내시겠습니까?".format(rock, scissors, paper))

    computer_choice = random.choice(list_a)

    print("당신은 {} 를 내고, 컴퓨터는 {} 를 냈습니다.".format(user_choice, computer_choice))

    if user_choice not in list_a:
        print("가위, 바위, 보 중에서 하나를 선택해주세요.")



    elif user_choice == computer_choice:
        print("무승부입니다.")

    elif ((user_choice == rock and computer_choice == scissors)
     or (user_choice == scissors and computer_choice == paper)
     or (user_choice == paper and computer_choice == rock)):
     win_score = win_score + 1
     print("당신이 이겼습니다.")


    else:
        lose_score = lose_score + 1
        print("당신이 졌습니다.")

if win_score == 2:
    print("당신이 최종승리했습니다.")

elif lose_score == 2:
    print("컴퓨터 최종승리. 가위바위보 빠카다네~")
