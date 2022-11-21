from rhbuck_tools.string_manipulation.is_palindrome import is_palindrome


def find_palindrome(num_of_digits):
    # Define a and b as variables
    a = int(str(9)*num_of_digits)
    b = int(str(9)*num_of_digits)

    # Degermine the lowest _num
    lowest_num = int(str(9)*(num_of_digits-1))

    largest_palindrome = 0
    for i in range(a, lowest_num, -1):
        for j in range(b, lowest_num, -1):
            if is_palindrome(i*j):
                if i * j > largest_palindrome:
                    largest_palindrome = i * j

    return largest_palindrome


if __name__ == "__main__":
    print(find_palindrome(3))