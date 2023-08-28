def divisible_by_three(s):
    result = 0
    arr = list(s)
    for i in range(len(arr)):
        original = arr[i]
        for n in range(10):
            arr[i] = str(n)
            num = int("".join(arr))
            if num % 3 == 0:
                result += 1
        arr[i] = original
    return result

def main():
    print(divisible_by_three("23")) # 7
    print(divisible_by_three("235")) # 9

if __name__ == "__main__":
    main()
