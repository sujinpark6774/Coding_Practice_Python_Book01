# 12-2. 문자열 재정렬

input_s = input()
# K1KA5CB7
# AJKDLSI412K4JSJ9D

string = "".join(sorted(input_s))
num_sum = 0
for i in range(len(string)):        # 알파벳 시작 추출
    if string[i].isalpha() == True:
        num = i
        break
    else:
        num_sum += int(string[i])

print(string[num:] + str(num_sum))