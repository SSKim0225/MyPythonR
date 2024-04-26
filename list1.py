import random


while True:
    input_N = int(input("N값을 입력하세요 (1-100): "))
    if 1 <= input_N <= 100:
        break
    
    print("N은 1 이상 100 이하의 정수여야 합니다.")

list_num = []
for i in range(0, input_N): # 0, 1, 2, 3, 4
    
    while True:
        random_num = random.randint(1,10)
        a = False
        for n in range(0, i):
            if list_num[n] == random_num:
                a = True
                break
        if not a :
            list_num.append(random_num)
            break
        

print(list_num)

while True:
    input_v = int(input(f"원하는 원소의 인덱스를 입력하세요 (0-{input_N-1}): "))
    if 0 <= input_v < len(list_num):
        print(f"선택한 인덱스의 원소: {list_num[input_v]}")
        break
    else:
        print("에러: 유효한 인덱스 범위를 벗어났습니다.")