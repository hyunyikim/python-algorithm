# 출처 프로그래머스 : https://programmers.co.kr/learn/courses/30/lessons/12912?language=python3


def solution(a, b):
    answer = 0
    if a == b: answer = a
    elif a < b:
        while a <= b:
            answer += a
            a += 1
    elif a > b:
        while a >= b:
            answer += b
            b += 1

    print(answer)
    return answer


# 다른 사람 풀이
def adder(a, b):
    if a > b: a, b = b, a
    return sum(range(a,b+1))

def adder2(a, b):
    return sum(range(min(a,b),max(a,b)+1))


solution(3, 5)
solution(7, 3)
solution(3, 3)