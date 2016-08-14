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


def test_num(n):
    """Test if an integer, n reduces to 1 applying the rules.

    if n is even, divide it by two, and if n is odd, 3n+1.
    """
    steps = 0
    new_value = n
    print(str(n) + '  '),

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
                print(Bcolors.RED + str(new_value) + '  ' + Bcolors.ENDC),
            else:
                print(Bcolors.GREEN + str(new_value) + '  ' + Bcolors.ENDC),
        else:
            new_value = new_value * 3 + 1
            if new_value < old_value:
                print(Bcolors.RED + str(new_value) + '  ' + Bcolors.ENDC),
            else:
                print(Bcolors.GREEN + str(new_value) + '  ' + Bcolors.ENDC),
    if new_value == 1:
        print(str(n) + ' converged to 1 in ' + str(steps) + ' steps')


def test_range(init, final):
    """Test a range of numbers, using range with initial and final values."""
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


def test_range_dict(init, final):
    """Test a range of numbers, using range with initial and final values.

    Uses dict lookup to optimize calculation time.
    """
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
