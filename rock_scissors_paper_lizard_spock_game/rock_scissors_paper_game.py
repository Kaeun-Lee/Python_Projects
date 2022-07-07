import pygame, sys, random
from pygame.locals import *

# 함수
def eventProcess():
    global isActive, result, choiceUser, choiceCom
    for event in pygame.event.get():          # pygame의 모든 event를 가져옴
        if event.type == pygame.KEYDOWN:      # event type이 키가 눌렸을 때(<-> KEYUP : 키를 뗀 것) 밑에 키들을 가져옴
            if event.key == pygame.K_ESCAPE:  # 프로그램 종료
                isActive = False              # False로 종료
                sys.exit()  # exit 메소드를 호출하며 모든 자원을 OS에 반환함. 즉 정상종료
                # pygame.quit()               # 이걸 하면, eventProcess()가 종료된 뒤, pygame.display.flip()를 하려다보니 에러가 발생
            if result == -1:
                if event.key == pygame.K_LEFT:    # 가위
                    choiceUser = 0
                if event.key == pygame.K_DOWN:    # 바위
                    choiceUser = 1
                if event.key == pygame.K_RIGHT:   # 보
                    choiceUser = 2
                if choiceUser != -1:
                    resultProcess()               # User 값이 -1이 아닌 값이 들어왔을 때 resultProcess()함수 호출
            else:                                 # 결과가 나왔을 때 재시작
                if event.key == pygame.K_SPACE:   # 재시작
                    result, choiceUser, choiceCom = -1, -1, -1          

def resultProcess():
    global result, win, lose, draw, choiceCom, choiceUser
    choiceCom = random.randint(0, 2)
    if choiceCom == choiceUser:
        result = 0
        draw += 1
    elif (choiceUser == 0 and choiceCom == 2)\
            or (choiceUser == 1 and choiceCom == 0)\
            or (choiceUser == 2 and choiceCom == 1):
        result = 1
        win += 1
    else:
        result = 2
        lose += 1

def setText():
    global result, win, lose, draw
    mFont = pygame.font.SysFont("굴림",  20)
    mtext = mFont.render(f'win {win}, lose {lose}, draw {draw}', True, 'green')
    SCREEN.blit(mtext, (10, 10, 0, 0))  # 위치(위에서 10, 밑에서 10, size, size)

    # 키보드 위치 조정
    mFont = pygame.font.SysFont("arial", 15)
    mtext = mFont.render(
        f'(scissors : ←)  (rock : ↓)  (paper : →)  (continue : space)', True, 'black')
    SCREEN.blit(mtext, (CENTER_WIDTH-30, 10, 0, 0))  # 길이 : 가운데에서 왼쪽으로 -40 당김

    # VS
    mFont = pygame.font.SysFont("arial", 60)
    mtext = mFont.render(f'VS', True, 'seagreen')
    SCREEN.blit(mtext, (CENTER_WIDTH-35, CENTER_HEIGHT-40, 0, 0))

    mFont = pygame.font.SysFont("arial", 30)
    mtext = mFont.render(f'      Comtuper                  User', True, 'black')
    SCREEN.blit(mtext, (CENTER_WIDTH-200, CENTER_HEIGHT-100, 0, 0))

    if result != -1:  # 결과가 있을 때 출력
        mFont = pygame.font.SysFont("arial", 50)
        resultText = ['Draw!!', 'Win!!', 'Lose']
        mtext = mFont.render(resultText[result], True, 'red')
        SCREEN.blit(mtext, (CENTER_WIDTH-53, CENTER_HEIGHT+70, 0, 0))

def getIndex():
    # Index를 호출하면 Time이 증가
    global updateTime, updateIndex
    if result == -1:  # result가 -1일 때(결과가 없을 때)만 update
        updateTime += 1
        if updateTime > 10:  # 1초(100ms * 10)주기로 계속 변경됨 -> 즉, 속도가 느려짐
            updateTime = 0  # 초기화
            updateIndex = (updateIndex+1) % len(player) # index를 1만큼 증가 그 범위를 나누기 연산으로 제한
        return updateIndex, updateIndex
    else: # 결과가 있다면
        return choiceCom, choiceUser  # 현재 Com과 User의 상태

def updatePlayer():  # 이미지 출력
    idx1, idx2 = getIndex()

    recPlayer[idx1].centerx = CENTER_WIDTH-100  # x의 center. img가 위치할 center의 위치 저장 # 컴퓨터의 이미지 / 가운데를 기준으로 왼쪽으로 -100만큼 이동
    recPlayer[idx2].centery = CENTER_HEIGHT     # 높이는 중간
    SCREEN.blit(player[idx1], recPlayer[idx1])
    
    recPlayer[idx2].centerx = CENTER_WIDTH+100  # 유저의 이미지 / 가운데를 기준으로 오른쪽에 100만큼 이동하여 그려짐
    recPlayer[idx2].centery = CENTER_HEIGHT
    SCREEN.blit(player[idx2], recPlayer[idx2])


# 변수 선언 및 초기화
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
CENTER_WIDTH = SCREEN_WIDTH/2    # screen의 중간 위치
CENTER_HEIGHT = SCREEN_HEIGHT/2  # screen의 중간 위치
isActive = True

updateTime = 0
updateIndex = 0

choiceUser, choiceCom = -1, -1  # 가위바위보 중 선택한 것을 넣음 / -1일 때는 선택하지 않았다는 의미를 명시
result = -1                     # 승, 패, 비김의 결과 / -1은 아직 결과가 없음을 명시
win, lose, draw = 0, 0, 0       # 몇 번을 이기고, 지고, 비겼는지 count / 나중에 결과로 출력

clock = pygame.time.Clock()


# pygame init
pygame.init()  # pygame 초기화
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # 게임 배경화면 생성 및 설정
pygame.display.set_caption('Rock Paper Scissors Lizard Spock!')  # 상단의 text


# 이미지 가져오기
# pImages = ['rock.jpg', 'scissors.jpg', 'paper.jpg' 'lizard.jpg', 'spock.jpg']
pImages = ['scissors.JPG', 'rock.JPG', 'paper.JPG']
player = [pygame.image.load('./images/'+ pImages[i]) for i in range(len(pImages))]
player = [pygame.transform.scale(player[i], (100, 100)) for i in range(len(player))]  # img size를 SCREEN size에 맞게 조정

recPlayer = [player[i].get_rect() for i in range(len(player))]  # 이미지를 어느 위치에 출력할 것인지 좌표 선언(생성)


# main loop
while(isActive): # screen을 update 하는 부분
    SCREEN.fill((255,255,255))  # 화면 그리기
    eventProcess() # event 하고
    updatePlayer() # 화면 그리고
    setText()      # 텍스트
    pygame.display.flip()  # 화면 update(갱신)
    clock.tick(100)  # framerate(초당 업데이트 횟수)