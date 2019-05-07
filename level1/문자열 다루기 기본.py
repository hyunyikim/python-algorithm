# 출처 프로그래머스 : https://programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    if(len(s) == 4 or len(s) == 6):
        if(s.isdigit()): return True
        else: return False
    else: return False


# 다른 사람 풀이
def solution2(s):
    return s.isdigit() and len(s) in (4, 6)


solution('1234d')