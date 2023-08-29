#그래프 경로
t = int(input())
for tc in range(1, t + 1):
    # 노드와 간선
    V, E = map(int, input().split())
    # 수식을 받아줄 수 있는 인접행렬을 구성해준다.
    adj_l = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    # 간선으로 이동할 경로를 받아줘야한다.

    for i in range(E):
        # 들어오는 인자 값이 두개씩 붙어서 들어오므로 나누어줄 수 있도록
        # input 을 설정
        s, e = map(int, input().split())
        # 간선으로 이동할 노드의 번호가 정해져야하는데
        # 쌍방향성인지 단방향성인지 고려를 하여 경로를 설정한다.
        # adj_l의 start(=s) 에 end(=e)값이 들어간다.
        adj_l[s].append(e)

    s_node, e_node = map(int, input().split())
    # 방향 설정를 해줬으니 간선들이 이동할 때의 경로를 볼 수 있는
    # visit 과 이전 값의 스텍을 볼 수 있는 스택변수
    # visit 배열을 만들어주고난 후에
    # 그리고 visit의 초기 값을설정해주고 진행해보자
    stack = []
    # visited는 일차원배열..?
    visited = [0 for _ in range(V + 1)]
    # 새로운 스타트 값을 지정해주는 변수를 지정
    # 인덱스 값으로 들어가므로 본인의 값을 그대로 받아올 수 있도록 입력
    ns = s_node

    # visited 한곳은 값을 1로 바꾸어줘라!
    visited[ns] = 1
    # 얼마나 반복될 지 모르니까 일단 계속 반복되게 해주고
    # 안의 조건문에서 반복문을 탈출하게 해줘라!
    ans = 0
    while True:
        # adj_l 안에 있는 것들중에서 비교해봐라
        for j in adj_l[ns]:

            if visited[j] == 0:
                visited[j] = 1
                # 스텍에 j값을 추가해줘야
                stack.append(j)
                ns = j
                # 만약의 그 j 값이 끝값과 같은지 비교하고
                if j == e_node:
                    # j값과 end 값이 같다면 갈수 있다고 표시하여라
                    ans = 1
        # 탐색을 다 했어도 이상하면 다른 경로확인

        else:
            # 스텍에 값이 있다면 스텍값을 빼고 돌아가라
            if stack:
                ns = stack.pop()
            else:
                break

    print(f"#{tc} {ans}")