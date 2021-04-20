#!/usr/bin/env python3


def default_printer(string_to_print):
    print(string_to_print)


def null_printer(string_to_print):
    pass


def fast_exp_with_explanation(base, exponent, mod_operand, printer=default_printer):
    if exponent < 1:
        printer("Exponent cannot be less than 1")
        return 0
    printer("Solve {}^{} mod {}".format(base, exponent, mod_operand))
    bins = []
    multiplicands = []
    printer("1. Compute partial results")
    num = exponent
    i = 0
    while num > 0:
        num_rem = num % 2
        val_raw = base if i == 0 else val_raw ** 2
        val_mod = val_raw % mod_operand
        printer(
            "[{0:2}] {1:10} ({2}) => {3:4}^(2^{0:2}) == {4:6} mod {5:4} == {6:4} mod {5:4}".format(
                i, num, num_rem, base, val_raw, mod_operand, val_mod
            )
        )
        num = num // 2
        val_raw = val_mod
        if num_rem == 1:
            multiplicands.append(val_mod)
        i += 1
    product_str = " * ".join([str(num) for num in multiplicands])
    result = 1
    printer("2. Compute final product")
    for num in multiplicands:
        result = (result * num) % mod_operand
    printer(
        "{0} ^ {1} mod {2} == {3} mod {2} = {4}".format(
            base, exponent, mod_operand, product_str, result
        )
    )
    return result


def run_test_suite():
    test_fast_exp_with_explanation(3, 123, 51, 24, default_printer)
    print(
        "[Further function calls will not print commentary text to stdout as sideeffect]"
    )
    test_fast_exp_with_explanation(6, 75, 78, 60, null_printer)
    test_fast_exp_with_explanation(8, 23, 100, 12, null_printer)
    test_fast_exp_with_explanation(11, 123, 45, 26, null_printer)
    test_fast_exp_with_explanation(7, 49, 10, 7, null_printer)


def test_fast_exp_with_explanation(base, exponent, mod_operand, expected, printer):
    print("-" * 80)
    print("CASE {} ^ {} mod {}".format(base, exponent, mod_operand))
    actual = fast_exp_with_explanation(base, exponent, mod_operand, printer)
    result_str = "PASS" if expected == actual else "FAIL"
    print("[{}] expected {} got {}".format(result_str, expected, actual))


def main():
    run_test_suite()


##############################################################################

if __name__ == "__main__":
    main()
