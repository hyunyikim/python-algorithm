# 출처 프로그래머스 : https://programmers.co.kr/learn/courses/30/lessons/12915?language=python3


def solution(strings, n):
    answer = []
    tmp = []
    strings.sort()
    for string in strings:
        tmp.append(string[n:])
    tmp.sort()

    for tmp_string in tmp:
        for string in strings:
            if string[n:] == tmp_string: answer.append(string)

    print(answer)
    return answer


solution(['sun', 'bed', 'car'], 1)
solution(['abce', 'abcd', 'cdx'], 2)