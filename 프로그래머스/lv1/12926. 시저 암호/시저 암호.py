def solution(s, n):
    st = "abcdefghijklmnopqrstuvwxyz"
    arr1 = list(st.lower())
    arr2 = list(st.upper())

    ans = []
    for i in s:
        if i in arr1:
            ans.append(arr1[(arr1.index(i)+n)% 26])
        elif i in arr2:
            ans.append(arr2[(arr2.index(i)+n)% 26])
        else:
            ans.append(i)

    return "".join(ans)
    