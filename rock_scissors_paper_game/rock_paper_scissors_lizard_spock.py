import random

print("===================================================================")
print("=================== 가위 바위 보 도마뱀 스팍게임 ==================")
print("===================================================================\n")


choice = ['가위', '바위', '보', '도마뱀', '스팍']
RULES = [("가위", "보"), ("보", "바위"), ("바위", "가위"), ("가위", "도마뱀"), 
        ("바위", "도마뱀"), ("보", "스팍"), ("도마뱀", "보"), ("도마뱀", "스팍"),
        ("스팍", "가위"), ("스팍", "바위")]


def get_num_player():
    while True:
        try:
            num_player = int(input("플레이어 수를 입력하세요. ex) 1, 2: "))
        except ValueError as e:
            num_player = 0
            print("숫자를 입력하세요! ", e)
        if num_player in [1, 2]:
            print(f"플레이어 수 : {num_player} 명")
            return num_player
        else:
            print("1과 2 중에서 하나를 선택하세요.")         


def get_num_round():
    while True:
        try:
            rounds = int(input("게임을 몇 번 진행할지 선택하세요. ex) 1, 3, 10... : "))
        except ValueError as e:
            rounds = 0
            print("숫자를 입력하세요! ", e)
        if rounds >= 1:
            return rounds
        else:
            print("0보다 큰 수를 입력하세요.")


def get_single_player_input():
    player1 = input('가위, 바위, 보, 도마뱀, 스팍 중 하나를 내세요. : ')
    player2 = choice[random.randint(0,2)]
    print(f"플레이어는 '{player1}'를, 컴퓨터는 '{player2}'를 냈습니다.")
    return player1, player2


def get_double_player_input():
    player1 = input('**첫 번째 플레이어** 가위, 바위, 보, 도마뱀, 스팍 중 하나를 내세요. : ')
    player2 = input('**두 번째 플레이어** 가위, 바위, 보, 도마뱀, 스팍 중 하나를 내세요. : ')
    print(f"첫 번째 플레이어는 '{player1}'를, 두 번째 플레이어는 '{player2}'를 냈습니다.")
    return player1, player2


def get_winner(player1, player2):
    """첫 번째가 이겼는지, 두 번째가 이겼는지, 비겼는지를 output"""
    if (player1, player2) in RULES:
        return 'player1'
    elif (player2, player1) in RULES:
        return 'player2'
    else:
        return None


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


def main():
    num_player = get_num_player()
    is_pc = (num_player == 1)
    rounds = get_num_round()
    score_player1 = score_player2 = 0  # scoreboard

    for i in range(rounds):
        if is_pc:
            player1, player2 = get_single_player_input()
        else:
            player1, player2 = get_double_player_input()

        winner = get_winner(player1, player2)
        print_winner(winner, is_pc)

        if winner == 'player1':
            score_player1 += 1
        elif winner == 'player2':
            score_player2 += 1
        else:
            continue  # 비김

    print(f"플레이어 : {score_player1} 점, 컴퓨터 : {score_player2} 점")


if __name__ == "__main__":
    main()