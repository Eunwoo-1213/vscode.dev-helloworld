#20231552 이은우
# if
grade = float(input('1학기 평균 평점은?'))  
if 3.8 <=grade:
    print('축하합니다! 장학금 지급 대상자입니다.')
print('당신의 1학기 평균 평점 %.2f이다.' %(grade))

#20231552 이은우
# if else
n = int(input('정수 입력 >>'))
if n%2 ==0:
    print('%d은 짝수다.' % n)
else:
    print('%d은 홀수다.' % n)

    '''01-02comments.py
    안녕하세요''' # 삼중 따옴표: 여러 줄에 걸쳐 문자열을 처리
    
    #콤마로 구분하여 출력
    print('Hi,', 'Python')
    print('23000원은', '5000원 ?개', '1000원은 ?개')
    print('5000원', 23000 // 5000, '개')
    print('1000원', (23000%5000) // 1000, '개')

    #eval() 모든"실행 가능한 파이썬 문장의 문자열"을 실행
    eval('3 + 15 / 2')
    eval('4 * 3 % 5')

    eval("java * 3")
    eval('"java" * 3')

    28 // 3, 28 % 3
    divmod(28,3)

