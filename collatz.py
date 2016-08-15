"""Functions dealing with the Collatz conjecture."""


class Bcolors:
    """Perty colors."""

    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def validate_num(n):
    """Attempt to typecast n as an integer."""
    try:
        n = int(n)
    except:
        print('Error validating number.  Please only use positive integers.')
        return 0
    else:
        return n


def test_num(n):
    """Test if an integer, n reduces to 1 applying the rules.

    if n is even, divide it by two, and if n is odd, 3n+1.
    """
    n = validate_num(n)
    if n:
        steps = 0
        new_value = n
        print(str(n) + '  ', end='')

        while new_value != 1:
            if steps > 100000:
                print('Congratulations!  You may have disproved the conjecture!')
                print(n)
                break

            old_value = new_value
            steps += 1

            if new_value % 2 == 0:
                new_value = new_value / 2
                if new_value < old_value:
                    print(Bcolors.RED + str(new_value) + '  ' + Bcolors.ENDC, end='')
                else:
                    print(Bcolors.GREEN + str(new_value) + '  ' + Bcolors.ENDC, end='')
            else:
                new_value = new_value * 3 + 1
                if new_value < old_value:
                    print(Bcolors.RED + str(new_value) + '  ' + Bcolors.ENDC, end='')
                else:
                    print(Bcolors.GREEN + str(new_value) + '  ' + Bcolors.ENDC, end='')
        if new_value == 1:
            print('')
            print(str(n) + ' converged to 1 in ' + str(steps) + ' steps')
    else:
        print("Exiting function.")


def test_range(init, final):
    """Test a range of numbers, using range with initial and final values."""
    init = validate_num(init)
    final = validate_num(final)
    if init and final and final > init:
        final += 1
        for i in range(init, final):
            steps = 0
            new_value = i

            while new_value != 1:
                if steps > 10000:
                    print('10000 steps exceeded!  Investigate ' + str(i) +
                          ' furthur!')
                    break

                steps += 1
                if new_value % 2 == 0:
                    new_value = new_value / 2
                else:
                    new_value = new_value * 3 + 1

            print(str(i) + ' converged to 1 in ' + str(steps) + ' steps')
    else:
        print('Exiting function.')
        print('Example usage: test_range(1,1000)')


def test_range_dict(init, final):
    """Test a range of numbers, using range with initial and final values.

    Uses dict lookup to optimize calculation time.
    """
    init = validate_num(init)
    final = validate_num(final)
    if init and final and final > init:
        final += 1
        dict_nums = {}

        for i in range(init, final):
            steps = 0
            new_value = i

            while new_value != 1:
                if steps > 10000:
                    print('10000 steps exceeded!  Investigate ' + str(new_value) +
                          ' furthur!')
                    break

                if new_value in dict_nums:
                    dict_nums[i] = steps + dict_nums[new_value]
                    print(Bcolors.GREEN + str(i) + ' reached 1 in ' +
                          str(dict_nums[i]) + ' steps' + Bcolors.ENDC)
                    break
                else:
                    steps += 1
                    if new_value % 2 == 0:
                        new_value = new_value / 2
                    else:
                        new_value = new_value * 3 + 1
            else:
                dict_nums[i] = steps
                print(str(i) + ' converged to 1 in ' + str(dict_nums[i]) +
                      ' steps')
    else:
        print('Exiting function.')
        print('Example usage: test_range_dict(1,1000)')
