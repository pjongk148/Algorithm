def solution(record):
    word ={"Enter":"님이 들어왔습니다.",
    "Leave":"님이 나갔습니다."}

    """
    id를 dic형식으로 받아서 바꿔주면 될듯..?
    """

    nic_dic = dict()
    for i in record:
        tmp = i.split(" ")
        if len(tmp) == 3:
            nic_dic[tmp[1]] = tmp[2]

    ans = []
    for i in record:
        tmp = i.split(" ")
        if tmp[0] != "Change":
            ans.append(nic_dic[tmp[1]] + word[tmp[0]])

    return ans