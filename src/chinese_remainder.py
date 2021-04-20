#!/usr/bin/env python3


def default_printer(string_to_print):
    print(string_to_print)


def null_printer(string_to_print):
    pass


def prod(iterable_numbers):
    accu = 1
    for num in iterable_numbers:
        accu *= num
    return accu


def multiplier_to_ensure_mod(num, goal_mod_class, mod_operand):
    i = 1
    # just an arbitrary limit to stop infinite looping
    # in case erronous inputs were given
    accu = 0
    while i < 1000:
        accu += num
        if accu % mod_operand == goal_mod_class:
            return i
        i += 1
    raise NameError("multiplier_to_ensure_mod wasn't able to find a solution")


def chinese_remainder_with_explanation(equations, printer=default_printer):
    M = prod(eq[1] for eq in equations)
    sum_parts = []
    printer("1. Find all y_i values by solving eqs of form 'y_i * M_i = 1 mod m_i'")
    i = 0
    for eq in equations:
        a_i = eq[0]
        m_i = eq[1]
        M_i = int(M / eq[1])
        y_i = multiplier_to_ensure_mod(M_i, 1, m_i)
        sum_parts.append(([a_i, M_i, y_i], a_i * M_i * y_i))
        printer(
            "[{0:2}] y_{0} * M_{0} => {1:4} * {2:6} == 1 mod{3:3}".format(
                i, y_i, M_i, m_i
            )
        )
        i += 1
    printer("2. Compute sum")
    sum_expressions = []
    for sum_part in sum_parts:
        sum_expressions.append(" * ".join(str(num) for num in sum_part[0]))
    sum_part_str_symbolic = " + ".join(
        ["a_{0} * M_{0} * y_{0}".format(i) for i in range(0, len(equations))]
    )
    printer(" " + sum_part_str_symbolic + " =")
    sum_str_not_evaluated = " + ".join(sum_expressions)
    sum_str_evaluated = " + ".join(str(sum_part[1]) for sum_part in sum_parts)
    printer(" = {}".format(sum_str_not_evaluated))
    printer(" = {}".format(sum_str_evaluated))
    result = sum(sum_part[1] for sum_part in sum_parts)
    printer(" = {} mod {}".format(result, M))
    result = result % M
    printer(" = {}".format(result))
    return result


def run_test_suite():
    test_chinese_remainder_with_explanation(
        [(2, 3), (2, 8), (4, 11)], 26, default_printer
    )
    print(
        "[Further function calls will not print commentary text to stdout as sideeffect]"
    )
    test_chinese_remainder_with_explanation([(1, 2), (2, 3), (4, 5)], 29, null_printer)


def pretty_string_mod_eq_system(mod_equations):
    return "\n".join(
        "   x == {:3} (mod {:3})".format(eq[0], eq[1]) for eq in mod_equations
    )


def test_chinese_remainder_with_explanation(equations, expected, printer):
    print("-" * 80)
    print("CASE equation system is below in pretty form")
    print(pretty_string_mod_eq_system(equations))
    actual = chinese_remainder_with_explanation(equations, printer)
    result_str = "PASS" if expected == actual else "FAIL"
    print("[{}] expected {} got {}".format(result_str, expected, actual))


def main():
    run_test_suite()


##############################################################################

if __name__ == "__main__":
    main()
