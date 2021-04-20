#!/usr/bin/env python3


def default_printer(string_to_print):
    print(string_to_print)


def null_printer(string_to_print):
    pass


def extended_euclidean_with_explanation(num_a, num_b, printer=default_printer):
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
    xs = [1, 0]
    ys = [0, 1]
    printer("2. Recursively compute x and y (Init x to [1,0], y to [0,1])")
    printer("   x_k = q_k-1 * x_k-1 + x_k-2")
    printer("   y_k = q_k-1 * y_k-1 + y_k-2")
    n = 0
    for i in range(2, len(rems) - 1):
        xs.append(xs[-2] + quos[i - 1] * xs[-1])
        ys.append(ys[-2] + quos[i - 1] * ys[-1])
        n = i
    xs.append(None)
    ys.append(None)
    str_row_x = "x |" + " | ".join("{:>6}".format("-" if x is None else x) for x in xs)
    str_row_y = "y |" + " | ".join("{:>6}".format("-" if y is None else y) for y in ys)
    printer(str_row_k)
    printer(str_row_r)
    printer(str_row_q)
    printer(str_row_x)
    printer(str_row_y)
    printer("3. Find k for the last non 0 r column")
    printer("n = {}".format(n))
    printer("4. Compute the sign of x and y")
    x = xs[n] if n % 2 == 0 else -xs[n]
    y = -ys[n] if n % 2 == 0 else ys[n]
    printer("  x = (-1)^n     * x_n = (-1)^{} * {:4} = {}".format(n, xs[n], x))
    printer("  y = (-1)^(n+1) * y_n = (-1)^{} * {:4} = {}".format(n + 1, ys[n], y))
    if num_a < num_b:
        printer("4+1. We switched a and b, so we must now switch x and y back")
        (y, x) = (x, y)
    result = num_a * x + num_b * y
    printer("5. And at last we substitute the values and get")
    printer("  a * x + b * y =")
    printer("  = {} * {} + {} * {}".format(num_a, x, num_b, y))
    printer("  = {}".format(result))

    return (x, y)


def run_test_suite():
    test_extended_euclidean_with_explanation(141, 17, (7, -58), default_printer)
    print(
        "[Further function calls will not print commentary text to stdout as sideeffect]"
    )
    test_extended_euclidean_with_explanation(258, 8, (1, -32), null_printer)
    test_extended_euclidean_with_explanation(143, 7, (-2, 41), null_printer)
    test_extended_euclidean_with_explanation(5, 56, (-11, 1), null_printer)


def test_extended_euclidean_with_explanation(num_a, num_b, expected, printer):
    print("-" * 80)
    print("CASE a = {} b = {}".format(num_a, num_b))
    actual = extended_euclidean_with_explanation(num_a, num_b, printer)
    result_str = "PASS" if expected == actual else "FAIL"
    print("[{}] expected {} got {}".format(result_str, expected, actual))


def main():
    run_test_suite()


##############################################################################

if __name__ == "__main__":
    main()
