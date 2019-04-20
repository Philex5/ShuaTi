
import sys

if __name__ == '__main__':
    try:
        while True:
            steamBottleNum = int(sys.stdin.readline().strip())
            if steamBottleNum == 0:
                break
            count = 0
            while steamBottleNum >= 3:
                mod = steamBottleNum // 3  # 可以兑换的空瓶数
                reminder = steamBottleNum % 3  # 兑换剩下的空瓶数
                steamBottleNum = mod + reminder  # 兑换之后的空瓶数
                count += mod

            if steamBottleNum == 2:
                count += 1
            print(count)

    except:
        pass




