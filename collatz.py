"""Functions dealing with the Collatz conjecture."""


class Bcolors:
    """Perty colors."""

    HEADER = '\033[95m'
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
    while new_value != 1:
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
    print('Value of 1 reached after ' + str(steps) + ' steps')


def test_range(init, n):
    """Test a range of numbers."""
    n = n + 1
    dict_nums = {}
    for i in range(init, n):
        steps = 0
        new_value = i
        while new_value != 1:
            if new_value in dict_nums:
                dict_nums[i] = steps + dict_nums[new_value]
                print(Bcolors.GREEN + str(i) + ' reached 1 in ' + str(dict_nums[i]) + ' steps' + Bcolors.ENDC)
                break
            else:
                steps += 1
                if new_value % 2 == 0:
                    new_value = new_value / 2
                else:
                    new_value = new_value * 3 + 1
        else:
            dict_nums[i] = steps
            print(str(i) + ' reached 1 in ' + str(dict_nums[i]) + ' steps')
