def solution(id_list, report, k):
    """
    id_list를 dic형식으로 담아주고 중복제거 위해 list(set())
    report리스트 안에 내용을 발신할땐 발신:수신dic,수신:횟수 dic로 나누어서 +=1 씩 해줌
    k이상되는 dic값들에 대해 report 가 포함되면 메일 +1
    """
    mail_count = dict()
    report_dic = dict()
    report = list(set(report))

    for _ in id_list:
        mail_count[_] = 0
        report_dic[_] = []

    for _ in report:
        tmp = _.split(" ")
        report_dic[tmp[1]].append(tmp[0])

    for _ in report_dic.keys():
        if len(report_dic[_]) >= k:
            for member in report_dic[_]:
                mail_count[member] += 1

    ans = []
    for i in id_list:
        ans.append(mail_count[i])
    return ans