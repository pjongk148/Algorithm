def solution(cacheSize, cities):
    if cacheSize ==0:
        return len(cities) * 5
    
    cache_list = []
    count =0

    for i in cities:
        i = i.lower()
        if  i in cache_list:
            cache_list.remove(i)
            cache_list.append(i)
            count += 1

        else:
            if len(cache_list) == cacheSize:
                cache_list.pop(0)
                cache_list.append(i)
                count += 5
            else:
                cache_list.append(i)
                count += 5
    
    return count