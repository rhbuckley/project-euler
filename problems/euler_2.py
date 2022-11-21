def fibonacci_until(max_num):
    total = 0
    arr: list = []
    current_num = 1
    last_num = 1
    while current_num < max_num:
        arr.append(current_num)

        if current_num % 2 == 0:
            total += current_num

        cn = current_num
        current_num += last_num
        last_num = cn

    print(total)


if __name__ == "__main__":
    fibonacci_until(4000000)
