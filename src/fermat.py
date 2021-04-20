#!/usr/bin/env python3

import fastexp


def default_printer(string_to_print):
    print(string_to_print)


def null_printer(string_to_print):
    pass


def fermat_test_with_explanation(
    prime_candidate,
    numbers_to_test,
    printer=default_printer,
    fastexp_printer=default_printer,
):
    def fastexp_printer_indented(str_to_print):
        fastexp_printer("    " + str_to_print)

    for base in numbers_to_test:
        printer(
            "Fermat for {0} -> {0} ^ {1} == 1 mod {2}".format(
                base, prime_candidate - 1, prime_candidate
            )
        )
        fastexp_printer_indented("-" * 76)
        equiv_class = fastexp.fast_exp_with_explanation(
            base, prime_candidate - 1, prime_candidate, fastexp_printer_indented
        )
        fastexp_printer_indented("-" * 76)
        printer(
            "  So we got {0} -> {0} ^ {1} == 1 mod {2} = {3}".format(
                base, prime_candidate - 1, prime_candidate, equiv_class
            )
        )
        if equiv_class != 1:
            printer("This Fermat test didn't pass,")
            printer(
                "so we can be 100% sure that {} is not a prime and we can exit".format(
                    prime_candidate
                )
            )
            return False
        printer("  Fermat test passed for {}".format(base))
    printer(
        "All Fermat tests passed so we are somewhat sure that {} a prime, but not 100%".format(
            prime_candidate
        )
    )
    return True


def run_test_suite():
    test_fermat_test_with_explanation(
        341, [2, 3], False, default_printer, default_printer
    )
    print(
        "[Further function calls will not print commentary text to stdout as sideeffect]"
    )
    test_fermat_test_with_explanation(181, [5, 7], True, null_printer, null_printer)
    test_fermat_test_with_explanation(129, [2, 5], False, null_printer, null_printer)


def test_fermat_test_with_explanation(
    prime_candidate, numbers_to_test, expected, printer, fastexp_printer
):
    print("-" * 80)
    print(
        "CASE prime_candidate = {}, testnumbers={}".format(
            prime_candidate, str(numbers_to_test)
        )
    )
    actual = fermat_test_with_explanation(
        prime_candidate,
        numbers_to_test,
        printer=printer,
        fastexp_printer=fastexp_printer,
    )
    result_str = "PASS" if expected == actual else "FAIL"
    print("[{}] expected {} got {}".format(result_str, expected, actual))


def main():
    run_test_suite()


##############################################################################

if __name__ == "__main__":
    main()
