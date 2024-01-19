# 숫자를 제곱하는 함수

def square(num:int)->int:
    # int가 아니면 실패 -> int가 어떻게? 실패는 뭐지
    if isinstance(num, int)==False:
        return 0
    return num*num


# 파이썬, js는 동적타입 -> 헷갈림 정적타입으로
# 자바는 정적타입 -> 동적타입으로
# --> 서로 장단점이 있음 / 단점을 보완하려고 함