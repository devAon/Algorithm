import re
def solution(files):
    answer = [re.split(r"([0-9]+)", file) for file in files]
    answer = sorted(answer, key=lambda x:(x[0].lower(), int(x[1])))
    answer = ["".join(file) for file in answer]
    
    return answer
if __name__ == '__main__':
    files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
    print(solution(files))