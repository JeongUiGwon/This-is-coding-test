# 맵 크기 입력
n, m = map(int, input().split())

# 현재 캐릭터의 위치 및 방향 입력
x, y, direction = map(int, input().split())

# 이동 횟수 및 회전 횟수, 종료 여부 변수 선언
count = 1
turn_time = 0
finish = False

# 현재 캐릭터 위치 및 방문 여부 확인
d = [[0] * m for _ in range(n)]

# 현재 캐릭터 위치 및 좌표 방문 처리
d[x][y] = 1

# 전체 맵 정보 입력
map_infos = []
for i in range(n):
    map_infos.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 왼쪽으로 회전 함수
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 앞으로 전진 함수
def go_straight():
    global count
    global turn_time
    global x
    global y
    global finish
    next_x = x + dx[direction]
    next_y = y + dy[direction]

    # 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[next_x][next_y] == 0 and map_infos[next_x][next_y] == 0:
        d[next_x][next_y] = 1
        print("(" + str(x) + "," + str(y) + ") -> (" + str(next_x) + "," + str(next_y) + ")")
        x = next_x
        y = next_y
        count += 1

    # 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        next_x = x - dx[direction]
        next_y = y - dy[direction]

        # 뒤로 갈 수 있다면 이동하기
        if map_infos[next_x][next_y] == 0 and d[next_x][next_y] == 0:
            print("(" + str(x) + "," + str(y) + ") -> (" + str(next_x) + "," + str(next_y) + ")")
            x = next_x
            y = next_y

        # 뒤로 갈 수 없다면 종료
        else:
            finish = True
        turn_time = 0

# 시뮬레이션 시작
while finish == False:
    turn_left()
    go_straight()

# 정답 출력
print(count)