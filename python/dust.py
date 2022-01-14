dust = 70

if dust >= 150:
    print('매우나쁨')
elif 80 < dust <= 150:
    print('나쁨')
elif 30 < dust <= 80:
    print('보통')
else:
    print('좋음')


# 포맷팅 스트링
# 기본문자는 '따옴표로 감싸서 사용'
# print(f'{dust} 따옴표로 감싸서 사용한다.')
# print('{} 따옴표로 감싸서 사용한다.'.format(dust))
