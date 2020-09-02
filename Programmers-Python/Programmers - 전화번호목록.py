def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]:
            return False
    return True

if __name__ == '__main__':
    phone_book = ["119", "97674223", "1195524421"]
    print(solution(phone_book))