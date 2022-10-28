def solution(files):
    tmp = []
    head , number, tail= "","",""
    for file in files:
        for i in range(len(file)):
            # 1. 첫번째는 무조건 문자이므로, 첫번째 문자이후 숫자일 경우
            if file[i].isdigit():
                head = file[:i]
                number = file[i:]

                for  j in range(len(number)):
                    if not number[j].isdigit():
                        tail = number[j:]
                        number = number[:j]
                        break
                tmp.append([head,number,tail])
                head, number, tail = '', '', ''
                break

        tmp.sort(key = lambda x : (x[0].lower(), int(x[1])))
    return ["".join(i) for i in tmp]