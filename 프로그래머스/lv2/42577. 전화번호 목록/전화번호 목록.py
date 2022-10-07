def solution(phone_book):
    phone_book.sort()
    for i in range(0,len(phone_book)-1):
        tmp = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][:tmp]:
            return False

        continue
    return True