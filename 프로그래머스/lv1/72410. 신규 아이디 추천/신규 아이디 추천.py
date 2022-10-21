def solution(new_id):
    #1. 대문자 -> 소문자
    new_id = new_id.lower()

    #2. 알파벳소문자, 숫자, - _ . 제외 모두 제거
    import re
    arr = []
    standard = re.compile("[a-zA-Z0-9-_.]")

    for i in new_id:
        if standard.match(i):
            arr.append(i)
    new_id = "".join(arr)

    #3. ..를 .로 치환
    while (".." in new_id):
        new_id = new_id.replace("..",".")

    #4. . 처음과 끝일 경우 제거
    new_id = new_id.strip(".")

    #5. 빈 문자열이면 a로 만듦
    if not new_id:
        new_id = "a"

    #6. 16자 이상이면 15개 이상 나머지 제거
    if len(new_id) >= 16:
        new_id = new_id[:15]

    #6-1. 제거 후 .가 맨끝이면 제거
    new_id = new_id.strip(".")

    #7. 길이 2자 이하면 마지막 문자 길이 3될때까지 반복해서 붙임
    if len(new_id) <= 2:
        new_id += new_id[-1] * (3- len(new_id))

    return new_id
    