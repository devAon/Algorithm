def solution(cacheSize, cities):
    answer = 0
    cache = []
    cities = [city.lower() for city in cities]
    
    for city in cities:
        if cacheSize == 0:
            answer = len(cities) * 5
            break
                
        if city in cache:
                cache.pop(cache.index(city))
                cache.append(city)
                answer += 1
        else: 
            if len(cache) < cacheSize:
                answer += 5
                cache.append(city)
            else:
                del cache[0]
                cache.append(city)
                answer += 5
        
    return answer

if __name__ == '__main__':
    cacheSize = 3
    cities = [ "Jeju",  "Pangyo ",  "Seoul ",  "NewYork ",  "LA ",  "Jeju ",  "Pangyo ",  "Seoul ",  "NewYork ",  "LA "]

    print(solution(cacheSize, cities))