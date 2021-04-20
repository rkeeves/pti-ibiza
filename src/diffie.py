#!/usr/bin/env python3

import fastexp


def default_printer(string_to_print):
    print(string_to_print)


def null_printer(string_to_print):
    pass


def diffie_with_explanation(
    large_prime,
    primitive_root,
    a_secret,
    b_secret,
    printer=default_printer,
    fastexp_printer=default_printer,
):
    def fastexp_printer_indented(str_to_print):
        fastexp_printer("       " + str_to_print)

    printer("1. Alice starts to compute her message to Bob")
    a_message_to_b = fastexp.fast_exp_with_explanation(
        primitive_root, a_secret, large_prime, fastexp_printer_indented
    )
    printer("   Alice got {}, she sends it to Bob".format(a_message_to_b))
    printer("2. Bob starts to compute his message to Alice")
    b_message_to_a = fastexp.fast_exp_with_explanation(
        primitive_root, b_secret, large_prime, fastexp_printer_indented
    )
    printer("   Bob got {}, he sends it to Alice".format(b_message_to_a))
    printer("3. Alice computes the symmetric key")
    a_symm_key = fastexp.fast_exp_with_explanation(
        b_message_to_a, a_secret, large_prime, fastexp_printer_indented
    )
    printer("   Alice computed the symmetric key = {}".format(a_symm_key))
    printer("4. Bob computes the symmetric key")
    b_symm_key = fastexp.fast_exp_with_explanation(
        a_message_to_b, b_secret, large_prime, fastexp_printer_indented
    )
    printer("   Bob computed the symmetric key = {}".format(b_symm_key))
    printer("5. Now both parties can use private key = {}".format(b_symm_key))
    return b_symm_key


def run_test_suite():
    test_diffie_with_explanation(149, 21, 3, 2, 82, default_printer, default_printer)
    print(
        "[Further function calls will not print commentary text to stdout as sideeffect]"
    )
    test_diffie_with_explanation(47, 11, 12, 23, 1, null_printer, null_printer)


def test_diffie_with_explanation(
    large_prime, primitive_root, a_secret, b_secret, expected, printer, fastexp_printer
):
    print("-" * 80)
    print(
        "CASE large_prime = {}, primitive_root={} a_secret={}, b_secret={}".format(
            large_prime, primitive_root, a_secret, b_secret
        )
    )
    actual = diffie_with_explanation(
        large_prime,
        primitive_root,
        a_secret,
        b_secret,
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
