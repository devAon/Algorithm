# import re
# import math

# def solution(str1, str2):
#     str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
#     str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

#     gyo = set(str1) & set(str2)
#     hap = set(str1) | set(str2)

#     if len(hap) == 0 :
#         return 65536

#     gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
#     hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

#     return math.floor((gyo_sum/hap_sum)*65536)


from collections import Counter

def solution(str1, str2):
    answer = 0
    arr1, arr2 = [],[]

    for i in range(len(str1)-1):
        s = str1[i]+str1[i+1]
        if s.isalpha():
            arr1.append(s.upper())

    for i in range(len(str2)-1):
        s = str2[i]+str2[i+1]
        if s.isalpha():
            arr2.append(s.upper())

    if len(arr1) == 0 and len(arr2) == 0:
        return 1 * 65536

    arr1Cnt, arr2Cnt = Counter(arr1), Counter(arr2)

    intersect = set(arr1) & set(arr2)
    union = set(arr1) | set(arr2)

    intersect =  sum([min(arr1Cnt[i], arr2Cnt[i]) for i in intersect])
    union = sum([max(arr1Cnt[i], arr2Cnt[i]) for i in union])    

    return int((intersect / union )  * 65536)



if __name__ == '__main__':
    str1 = "FRANCE"
    str2 = "french"
    print(solution(str1, str2))
    