#!/usr/bin/env python3


def default_printer(string_to_print):
    print(string_to_print)


def null_printer(string_to_print):
    pass


def euclidean_with_explanation(num_a, num_b, printer=default_printer):
    if num_a < num_b:
        printer("0. Number a was larger than b so we switch them")
        rems = [num_b, num_a]
    else:
        rems = [num_a, num_b]
    printer("1. Recursively solve the 'table' (init r to [a, b])")
    printer("  r_k = r_k-2 % r_k-1")
    printer("  q_k = r_k-1 // r_k")
    printer("    Where:")
    printer("      %  - mod operator")
    printer("      // - integer division")
    quos = [None]
    i = 0
    # just an arbitrary limit to stop infinite looping
    # in case erronous inputs were given
    while rems[-1] != 0 and i < 1000:
        r = rems[-2] % rems[-1]
        q = rems[-2] // rems[-1]
        rems.append(r)
        quos.append(q)
        i += 1
    quos.append(None)
    str_row_k = "k |" + " | ".join("{:>6}".format(k) for k in range(len(rems)))
    str_row_r = "r |" + " | ".join("{:>6}".format(r) for r in rems)
    str_row_q = "q |" + " | ".join(
        "{:>6}".format("-" if q is None else q) for q in quos
    )
    printer(str_row_k)
    printer(str_row_r)
    printer(str_row_q)
    return rems[-2]


def run_test_suite():
    test_euclidean_with_explanation(141, 17, 1, default_printer)
    print(
        "[Further function calls will not print commentary text to stdout as sideeffect]"
    )
    test_euclidean_with_explanation(45, 211, 1, null_printer)
    test_euclidean_with_explanation(1491, 23, 1, null_printer)
    test_euclidean_with_explanation(595, 867, 17, null_printer)


def test_euclidean_with_explanation(num_a, num_b, expected, printer):
    print("-" * 80)
    print("CASE a = {} b = {}".format(num_a, num_b))
    actual = euclidean_with_explanation(num_a, num_b, printer)
    result_str = "PASS" if expected == actual else "FAIL"
    print("[{}] expected {} got {}".format(result_str, expected, actual))


def main():
    run_test_suite()


##############################################################################

if __name__ == "__main__":
    main()
