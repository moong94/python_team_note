def possible(answer):
    for x, y, stuff in answer:
        # 기둥 설치
        if stuff == 0:
            # 바닥 위                    보의 한쪽 끝 위                      다른 기둥 위
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        # 보 설치
        elif stuff == 1:
            # 한쪽 끝 부분이 기둥 위                                      양쪽 끝 부분이 다른 보
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer \
                                                                          and [x + 1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for build in build_frame:
        x, y, stuff, op = build
        # 삭제
        if op == 0:
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        # 설치
        elif op == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.pop()

    answer.sort()

    return answer