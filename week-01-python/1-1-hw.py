
import random

# 1) 식당 리스트
korean_food = ("한식1", "한식2", "한식3")
chinese_food = ["중식1", "중식2", "중식3"]
japanese_food = ["일식1", "일식2", "일식3"]

# 2) 유저의 값
user_choice = input("한식, 중식, 일식 중 한가지를 고르세요 : ")

# 3) 랜덤 뽑기


if user_choice == "한식":
    choice_result = random.choice(korean_food)

elif user_choice == "중식":
    # print(random.choice(chinese_food))
    choice_result = random.choice(chinese_food)

elif user_choice == "일식":
    choice_result = random.choice(japanese_food)

else:
    print("한식, 중식, 일식 중에서 한가지를 고르셔야 합니다")

if choice_result:
    print("{} 중에서 {}가 추천되었습니다".format(user_choice, choice_result))
