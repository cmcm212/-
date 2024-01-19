from func001 import sample1, is_get, ticket, sale

# 테스트하는 함수를 작성
# 테스트하는 함수는 pytest로 실행이 가능
# unit test(함수 테스트)

#def test_smaple1():
#    assert sample1()==10       
     # assert는 확인하는 함수

#def test_round():
#    assert round(2.5)==3

#def test_is_get():
#    assert is_get(20) is True
#    assert is_get(18) is True
#    assert is_get(15) is False

#나이를 입력받아 입장료를 리턴하는 함수
# 25~64세면 3000원, 기타는 무료

#def test_ticket():
#    assert ticket(70)==0
#    assert ticket(25)==3000
#    assert ticket(30)==3000
#    assert ticket(64)==3000
#    assert ticket(24)==0

# 입장료는 3000원이다. 10명이면 1인당 2400원이다.
# 인원수를 입력받아 요금을 출력
    
def test_sale():
    assert sale(10)==24000
    assert sale(5)==15000
    assert sale(24)==57600
    assert sale(9)==27000