import re

content = "이것은 테스트 계약서\n\n\
목차 \n\
제 1조 계약의 목적\n\n 제 2조 계약의 정의\n\n 이제부터 본문입니다 \n\n 본문 \n\n\
제 1조 계약의 목적 \n 돈을 벌려고\n\n 제 2조 계약의 정의\n계약의 탐욕적인 것 \n\n\
 제 11 조 계약의 종료 \n 계약중 (제1조) 참고하세요\n\n끝 \n\
별첨입니다\n\
제 1조 계약의 목적\n 별첨하려고\n\n 제 2조 계약의 정의\n별첨하려고 \n\n\
이상입니다"

pat_prov = '\n\s*제\s*\d+\s*조'
pat_1st_prov = '제\s*1\s*조'
pat_next = '\n\n'
pt = re.compile(pat_prov)

def __is_body(check_content):
    return not (("목차" in check_content) or\
                ("붙임" in check_content) or\
                ("별첨" in check_content))

docu = []
docu_idx = [False]
before = 0
now_flag = 0
pre_flag = 0
items = pt.finditer(content)
for item in items:
    now_flag = item.span()[0]+1
    if re.search(pat_1st_prov, item.group()):
        if before > 0:
            pre_content = content[pre_flag:now_flag]
            cnt_flag = re.search(pat_next, pre_content).span()[0]+1
            docu.append(content[before:pre_flag+cnt_flag+1])
            docu_idx.append(False)
            split_content = content[pre_flag+cnt_flag+1:now_flag]
            docu.append(split_content)
            docu_idx.append(__is_body(split_content))
        else:
            split_content = content[before:now_flag]
            docu.append(split_content)
            docu_idx.append(__is_body(split_content))
            
        before = now_flag
    pre_flag = now_flag

pre_foot = content[now_flag:]
after = re.search(pat_next, pre_foot).span()[0]+1
docu.append(content[before:now_flag] + pre_foot[:after])
docu_idx.append(False)
docu.append(pre_foot[after:])

result = []
part = ""
i = 0
for part_docu in docu:
    if docu_idx[i]:
        result.append(part)
        result.append(part_docu)
        part = ""
    else:
        part+=part_docu
    i+=1
result.append(part)

for item in result:
    print("================")
    print(item)
