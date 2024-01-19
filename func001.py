def sample1():
    return 10

# 나이를 입력받아 성년/미성년을 판단

def is_get(age:int)->bool:
    return age>=18


#나이를 입력받아 입장료를 리턴하는 함수
# 25~64세면 3000원, 기타는 무료

def ticket(age:int)->int:
    if age>24 and age<65:
        return 3000
    return 0

def sale(people:int)->int:
    if people<10:
        return people*3000
    return people*2400