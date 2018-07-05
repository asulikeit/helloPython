import re

content = "이것은 테스트 계약서\n\n 목차 \n 제 1조 계약의 목적\n\n 제 2조 계약의 정의\n\n 본문 \n\n 제 1조 계약의 목적 \
\n 돈을 벌려고\n\n 제 2조 계약의 정의\n계약의 탐욕적인 것 \n\n 제 11 조 계약의 종료 \n 계약중 (제1조) 참고하세요\n\n끝 \n\
이상입니다"

pt = re.compile('\n\s*제\s*\d+\s*조')

tika = []
items = pt.finditer(content)
before = 0
now_flag = len(content)-1
for item in items:
    print(str(item))
    now_flag = item.span()[0]+1
    if re.search('제\s*1\s*조', item.group()):
        now_flag = item.span()[0]+1
        tika.append(content[before:now_flag])
        before = now_flag

pre_foot = content[now_flag:]        
after = re.search('\n\n', pre_foot).span()[0]+1
tika.append(content[before:now_flag] + pre_foot[:after])
tika.append(pre_foot[after:])
print(str(tika))