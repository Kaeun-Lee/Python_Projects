import random

print("==========================================================")
print("=================== 가위 바위 보 게임 ====================")
print("==========================================================\n")


choice = ['가위', '바위', '보']


def number_player():
    while True:
        num_player = int(input("플레이어 수를 입력해 주세요. ex) 1, 2 : "))
        if num_player in [1,2]: 
            return num_player
        else:
            print("1과 2 중 하나를 선택해 주세요.")


def scoreboard():
    while True:
        rounds = int(input("게임을 몇 번 진행할지 선택해 주세요. ex) 1, 3, 10... : "))
        if rounds > 1:
            return rounds
        else:
            print("0보다 큰 수를 입력하세요.")


def single_player():
    player1 = input('가위, 바위, 보 중 하나를 내세요. : ')
    player2 = choice[random.randint(0,2)]
    print(f"플레이어는 '{player1}'를, 컴퓨터는 '{player2}'를 냈습니다.")
    return player1, player2


def double_player():
    player1 = input('**첫 번째 플레이어** 가위, 바위, 보 중 하나를 내세요. : ')
    player2 = input('**두 번째 플레이어** 가위, 바위, 보 중 하나를 내세요. : ')
    print(f"첫 번째 플레이어는 '{player1}'를, 두 번째 플레이어는 '{player2}'를 냈습니다.")
    return player1, player2


def play(rounds, num_player):
    score_player1 = score_player2 = 0

    for i in range(rounds):
        if num_player == 1:
            player1, player2 = single_player()
        else:
            player1, player2 = double_player()
        
        if player1 == '가위':
            if player2 == '바위':
                print("player2가 이겼습니다.")
                score_player2 += 1
            elif player2 == '보':
                print("사용자가 이겼습니다!")
                score_player1 += 1
            else:
                print("비겼습니다.")

            print(score_player1, score_player2)

        elif player1 == '바위':
            if player2 == '보':
                print("컴퓨터가 이겼습니다.")
                score_player2 += 1
            elif player2 == '가위':
                print("사용자가 이겼습니다!")
                score_player1 += 1
            else:
                print("비겼습니다.")

            print(score_player1, score_player2)

        else:
            if player2 == '가위':
                print("컴퓨터가 이겼습니다.")
                score_player2 += 1
            elif player2 == '바위':
                print("사용자가 이겼습니다!")
                score_player1 += 1
            else:
                print("비겼습니다.")
            
            print(score_player1, score_player2)

    print(f"플레이어 : {score_player1} 점, 컴퓨터 : {score_player2} 점")

num_player = number_player()
print(num_player)
rounds = scoreboard()
print(rounds)
play(rounds, num_player)





