def solution(brown, yellow):
    for i in range(1, int(yellow**0.5)+1):
        if not yellow % i:
            j = yellow // i
            if 2*i + 2*j + 4 == brown:
                return [j+2, i+2]