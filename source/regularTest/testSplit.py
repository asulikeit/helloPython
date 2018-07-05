import re

content = "이것은 테스트 계약서\n\n\
목차 \n\
제 1조 계약의 목적\n\n 제 2조 계약의 정의\n\n 이제부터 본문입니다 \n\n 본문 \n\n\
제 1조 계약의 목적 \n 돈을 벌려고\n\n 제 2조 계약의 정의\n계약의 탐욕적인 것 \n\n\
 제 11 조 계약의 종료 \n 계약중 (제1조) 참고하세요\n\n끝 \n\
별첨입니다\n\
제 1조 계약의 목적\n 별첨하려고\n\n 제 2조 계약의 정의\n별첨하려고 \n\n\
이상입니다"

pt = re.compile('\n\s*제\s*\d+\s*조')

tika = []
items = pt.finditer(content)
before = 0
now_flag = len(content)-1
pre_flag = 0
for item in items:
    now_flag = item.span()[0]+1
    if re.search('제\s*1\s*조', item.group()):
        if before > 0:
            pre_content = content[pre_flag:now_flag]
            cnt_flag = re.search('\n\n', pre_content).span()[0]+1
            tika.append(content[before:pre_flag+cnt_flag+1])
            tika.append(content[pre_flag+cnt_flag+1:now_flag])
        else:
            tika.append(content[before:now_flag])
        before = now_flag
    pre_flag = now_flag

pre_foot = content[now_flag:]
after = re.search('\n\n', pre_foot).span()[0]+1
tika.append(content[before:now_flag] + pre_foot[:after])
tika.append(pre_foot[after:])

i = 0
for cnt in tika:
    i+=1
    print(i, "======\n", cnt)