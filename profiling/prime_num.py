

def check_if_prime(number: int) -> bool:
    '''
    _summary_

    Parameters
    ----------
    number : int
        _description_

    Returns
    -------
    bool
        _description_
    '''
    result = True
    for i in range(2, number):
        if number % i == 0:
            result = False
    return result


if __name__ == "__main__":

    PRIMES = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
              41, 43, 47,53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    NUM_PRIMES_UP_TO = 100
    primes = [num for num in range(1, NUM_PRIMES_UP_TO) if check_if_prime(num)]
    assert primes[:len(PRIMES)] == PRIMES
    print("PRIMES")
    print("======")
    for p in primes:
        print(p)
    print("=======")
