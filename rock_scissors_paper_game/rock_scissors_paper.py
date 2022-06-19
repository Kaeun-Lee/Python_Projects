import random

print("==========================================================")
print("=================== 가위 바위 보 게임 ====================")
print("==========================================================\n")


choice = ['가위', '바위', '보']


def get_num_player():
    while True:
        num_player = int(input("플레이어 수를 입력해 주세요. ex) 1, 2 : "))
        if num_player in [1,2]: 
            return num_player
        else:
            print("1과 2 중 하나를 선택해 주세요.")


def get_num_round():
    while True:
        rounds = int(input("게임을 몇 번 진행할지 선택해 주세요. ex) 1, 3, 10... : "))
        if rounds > 1:
            return rounds
        else:
            print("0보다 큰 수를 입력하세요.")


def get_single_player_input():
    player1 = input('가위, 바위, 보 중 하나를 내세요. : ')
    player2 = choice[random.randint(0,2)]
    print(f"플레이어는 '{player1}'를, 컴퓨터는 '{player2}'를 냈습니다.")
    return player1, player2


def get_double_player_input():
    player1 = input('**첫 번째 플레이어** 가위, 바위, 보 중 하나를 내세요. : ')
    player2 = input('**두 번째 플레이어** 가위, 바위, 보 중 하나를 내세요. : ')
    print(f"첫 번째 플레이어는 '{player1}'를, 두 번째 플레이어는 '{player2}'를 냈습니다.")
    return player1, player2


def get_winner(player1, player2):
    """첫 번째가 이겼는지, 두 번째가 이겼는지, 비겼는지를 output"""
    score_player1 = score_player2 = 0

    if player1 == player2:
        winner = None
        return winner
    else:
        if player1 == '가위':
            if player2 == '바위':
                winner = 'player2'
                score_player2 += 1
            else:
                winner = 'player1'
                score_player1 += 1
            return winner

        elif player1 == '바위':
            if player2 == '보':
                winner = 'player2'
                score_player2 += 1
            else:
                winner = 'player1'
                score_player1 += 1
            return winner

        else:
            if player2 == '가위':
                winner = 'player2'
                score_player2 += 1
            else:
                winner = 'player1'
                score_player1 += 1
            return winner

    print(f"플레이어 : {score_player1} 점, 컴퓨터 : {score_player2} 점")

def print_winner(winner, is_pc):
    """
    주어진 input에 따라 print 하는 문구가 달라짐.
    is_pc가 참이면, 컴퓨터와 하는 1인 게임, 거짓이면 둘이서 하는 2인 게임.
    """
    if winner is None:
        print("비겼습니다.")
    else:
        if is_pc:
            if winner == "player1":
                print("플레이어가 이겼습니다!")
            else: 
                print("컴퓨터가 이겼습니다!")
        else:
            if winner == "player1":
                print("첫 번째 플레이어가 이겼습니다!")
            else:
                print("두 번째 플레이어가 이겼습니다!")


num_player = get_num_player()
is_pc = (num_player == 1)
rounds = get_num_round()


for i in range(rounds):
    if is_pc:
        player1, player2 = get_single_player_input()
    else:
        player1, player2 = get_double_player_input()

    winner = get_winner(player1, player2)
    print_winner(winner, is_pc)