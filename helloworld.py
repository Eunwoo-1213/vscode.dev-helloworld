#20231552 이은우
while True:
    menu = input('[0]종료 [1]계속?')
    if menu == '0':
        break
print('종료')

#20231552 이은우
days = ['monday', 'tuesday', 'wednesday']

while True:
    user = input('월, 화, 수 중 하나 영어 단어 입력 >>')
    if user not in days:
        print('잘못 입력했어요!')
        continue
    print('입력: %s, 철자가 맞습니다' %user)
    break

print(' 종료 '.center(15, '*'))
