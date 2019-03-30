# 출처 프로그래머스 : https://programmers.co.kr/learn/courses/30/lessons/12922?language=python3


def solution(n):
    answer = ''
    s = '수박'

    div, mod = divmod(n, s.__len__())
    answer += s * div
    if mod == 1: answer += s[mod - 1]
    return answer


# 다른 사람 풀이
def water_melon(n):
    s = "수박" * n
    return s[:n]

def water_melon2(n):
    return "수박"*(n//2) + "수"*(n%2)


solution(4)
solution(9)