# 출처 프로그래머스 : https://programmers.co.kr/learn/courses/30/lessons/12916?language=python3


def solution(s):
    answer = True
    p_num = 0
    y_num = 0

    for i in s.lower():
        if i == 'p': p_num += 1
        elif i == 'y': y_num += 1
    if p_num == y_num: answer = True
    elif p_num != y_num: answer = False

    return answer


# 다른 사람 풀이
def solutio2(s):
    return s.lower().count('p') == s.lower().count('y')


solution('Hello Python')
solution('ppyyy')
