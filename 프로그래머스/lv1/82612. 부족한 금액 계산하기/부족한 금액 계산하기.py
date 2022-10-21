def solution(price, money, count):
    ans = sum([price * i for i in range(1,count+1)])
    return ans-money  if ans >money  else 0