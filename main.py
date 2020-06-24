from random import randint # 랜덤 프로그램 만들기
t = ["Rock", "Paper", "Scissor"] # 가위 바위 보 재생 옵션 변수 입력
computer = t[randint(0, 2)] #컴퓨터에 무작위로 3가지 가능한 플레이 할당 하다
player = False

while player == False : # 루프 문 while
   player = int("Rork, Paper, Scissors?")
   if player == computer :
       print("Tie")
    elif player == "Rock": # 플레이어가 주먹 
        if computer == "Paper" : # 컴퓨터가 보 일때
            print("You lose", computer, "covers", player)
        else :
            print("You win!", player , "smashes", computer)
    elif player == "Paper": # 플레이어가 보 일때
        if computer == "Scissors": # 컴퓨터가 가위 일때
            print("You losr!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors": # 플레이어가 가위 일때
        if computer == "Rock": # 컴퓨터가 주먹일때
            print("You lose.....", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's no valid play. Check your spelling!")

    player = False
    computer = t[randint(0,2)] 
    