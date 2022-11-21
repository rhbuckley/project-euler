from functools import reduce


def largest_product_in_series(sseries: int, digits: int) -> int:
    """
    This is my attempt at euler 8. This problem requires you to find
    the largest product in a series, and although we could easily
    multiply and hold a max value, we can also just look for the largest
    sum of digits, and then multiply them at the end.
    :param sseries: a series of numbers
    :param digits: the number of consecutive digits to search for
    :return: largest product in series
    """
    # Define Variables
    largest_sum: int = 0
    ls_index: int = 0

    # Convert series to list
    series_list = list(map(int, str(sseries)))

    # for number in series ...
    for i in range(0, len(series_list) - digits, 1):
        # define starting and ending index
        si, ei = i, i + digits
        # define series list as sl
        sl = series_list[si: ei]
        # define sum_num as sum
        sum_num = sum(sl)
        # if sum_num is larger than the greatest sum
        if sum_num > largest_sum:
            # we do not want any 0s in our product
            if 0 in sl: continue

            # if 1 is in series list
            if 1 in sl:
                # check if the stored product is greater than the current product
                this = reduce((lambda x, y: x * y), sl)
                stored = reduce((lambda x, y: x * y), series_list[ls_index: ls_index + digits])
                # if the stored product is larger continue the function
                if stored > this: continue

            # set the largest_sum to sum_num and update index
            largest_sum = sum_num
            ls_index = i

    # return the result
    res = series_list[ls_index: ls_index + digits]
    # check to make sure we have the right result
    return reduce((lambda x, y: x * y), series_list[ls_index: ls_index+digits])


if __name__ == "__main__":
    series = int("""
             73167176531330624919225119674426574742355349194934
             96983520312774506326239578318016984801869478851843
             85861560789112949495459501737958331952853208805511
             12540698747158523863050715693290963295227443043557
             66896648950445244523161731856403098711121722383113
             62229893423380308135336276614282806444486645238749
             30358907296290491560440772390713810515859307960866
             70172427121883998797908792274921901699720888093776
             65727333001053367881220235421809751254540594752243
             52584907711670556013604839586446706324415722155397
             53697817977846174064955149290862569321978468622482
             83972241375657056057490261407972968652414535100474
             82166370484403199890008895243450658541227588666881
             16427171479924442928230863465674813919123162824586
             17866458359124566529476545682848912883142607690042
             24219022671055626321111109370544217506941658960408
             07198403850962455444362981230987879927244284909188
             84580156166097919133875499200524063689912560717606
             05886116467109405077541002256983155200055935729725
             71636269561882670428252483600823257530420752963450
             """.replace("\n", "").replace(" ", ""))
    print(largest_product_in_series(series, 13))
