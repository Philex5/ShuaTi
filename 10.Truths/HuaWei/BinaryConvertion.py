
import sys

if __name__ == '__main__':
    try:
        while True:
            # 使用内置函数，太没意思了吧
            # convertedNum = int(sys.stdin.readline().strip(), 16)
            # print(convertedNum)
            # 自己实现
            stringNum = sys.stdin.readline().strip()
            if stringNum[:2] != '0x':
                raise ValueError
            num = 0
            for i in range(len(stringNum)-1, 1, -1):
                if 'A' <= stringNum[i] <= 'F':
                    num += (10 + ord(stringNum[i]) - 65) * (16 ** (len(stringNum)-1-i))
                else:
                    num += int(stringNum[i]) * (16 ** (len(stringNum - 1) - i))

            print(num)

    except :
        pass