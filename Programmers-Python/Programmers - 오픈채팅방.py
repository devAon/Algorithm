def solution(record):
    userDic = dict() # 유저아이디, 닉네임
    chat = []
    answer = []
    
    for dataList in record : # data[0] : Enter ,Leave , Change  /[1] : uid1234 , uid4567  /[2] : Muzi, Prodo
        data = dataList.split()
        if data[0] == "Enter":
            userDic[data[1]] = data[2]
            chat.append([data[1], "님이 들어왔습니다."])
        elif data[0] == "Leave":
            chat.append([data[1], "님이 나갔습니다."])
        elif data[0] == "Change":
            userDic[data[1]] = data[2]

    for chatData in chat:
        answer.append(userDic[chatData[0]]+chatData[1])
    return answer



# main
record=  ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))