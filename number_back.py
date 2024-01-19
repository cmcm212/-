# 데이터 자체는 원래는 백이 아니라 database에서 관리
# front는 사용자와 입출력하는 view를 담당(터미널, 웹, 안드로이드, 아이폰)
# 백은 처리를 담당하고 view와 상관없이 재사용하고 싶다.
# 백을 재사용하려면 백에는 절대 view 관련 코드가 없어야 한다.
numbers = []

def save(num:int)->bool:
    if isinstance(num, int)==False:     # is 가 있으면 결과값은 참/것짓
        return False
    numbers.append(num)     # return이 없으면 테스트가 불가능함.
    return True

def find_all()->list:
    return numbers

def delete(num:int)->bool:
    if isinstance(num,int)==False:
        return False
    for item in numbers:
        if item==num:
            numbers.remove(item)
            return True
    return False