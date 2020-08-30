# 90도 회전
def rotate_a_matrix_by_90_degree(a):
    n = len(a) 
    m = len(a[0])
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result
    
# 자물쇠 중간 부분이 모두 1인지 확인
def check(new_lock):
    length = len(new_lock) // 3
    for i in range(length, length * 2):
        for j in range(length, length * 2):
            if new_lock[i][j] != 1:
                return False
    return True
    
def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
            
    # 4 방향 확인
    for rotation in range(4):
        key= rotate_a_matrix_by_90_degree(key) # 열쇠회전
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                
                if check(new_lock) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False

if __name__ == '__main__':
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(solution(key, lock))
    