#!/usr/bin/env python3

import fastexp


def default_printer(string_to_print):
    print(string_to_print)


def null_printer(string_to_print):
    pass


def miller_rabin_with_explanation(
    prime_candidate, numbers_to_test, printer=default_printer
):

    if prime_candidate < 2 or prime_candidate % 2 == 0:
        printer("This prime test works for odd numbers greater than 1. :)")
        return False
    printer("1. Compute S, such that")
    rs = []
    nsub1 = prime_candidate - 1
    r = 0
    val = 1
    while val <= nsub1:
        if (nsub1 % val) == 0:
            rs.append(r)
        r += 1
        val *= 2
    S = max(rs)
    printer("   S =")
    raisedS = 2 ** S
    d = nsub1 // raisedS
    printer("  = max( {r| 2^r divides (n - 1)} ) =")
    printer("  = max( {{r| 2^r divides ({} - 1)}} ) =".format(prime_candidate))
    printer("  = max( {{r| 2^r divides ({})}} ) =".format(nsub1))
    printer("  = max({})".format(str(rs)))
    printer("  = {}".format(max(rs)))
    printer("2. Compute d, such that")
    printer("  d =")
    printer("  = (n-1) * (2 ^ S)")
    printer("  = ({}-1) * (2 ^ {})".format(prime_candidate, S))
    printer("  = {} * (2 ^ {})".format(nsub1, S))
    printer("  = {} * {}".format(nsub1, raisedS))
    printer("  = {}".format(d))
    printer("3. Thus S={} and d={}.".format(S, d))
    printer(
        "4. We loop through all bases from {} and checl the following:".format(
            str(numbers_to_test)
        )
    )
    printer("  If {0} is prime and gcd(base, {0}) = 1".format(prime_candidate))
    printer("  Then either")
    printer("    - base^{0} == 1 mod {1}".format(d, prime_candidate))
    r_range = [e for e in range(0, S)]
    printer(
        "    - there exists r in {2} such that base^({0}^(2^r)) == -1 mod {1}".format(
            d, prime_candidate, str(r_range)
        )
    )

    for base in numbers_to_test:
        printer("    Base {}".format(base))
        result = fastexp.fast_exp_with_explanation(
            base, d, prime_candidate, null_printer
        )
        printer(
            "      First Check: {0}^{1} == 1 mod {2} = {3} ?== 1".format(
                base, d, prime_candidate, result
            )
        )
        if result == 1:
            printer(
                "      Passed, so it can be a prime, we go to next base".format(
                    d, prime_candidate
                )
            )
            continue
        printer(
            "      Failed, so we continue checking different r values from {}".format(
                str(r_range)
            )
        )
        encountered_solution = False
        for r in r_range:
            printer("        Check r = {}".format(r))
            result = fastexp.fast_exp_with_explanation(
                base, d * (2 ** r), prime_candidate, null_printer
            )
            printer(
                "        {0:<} ^ ({1}*(2^{2})) = {0} ^ ({1}*{3}) = {0} ^ {4} = {5} ?== -1 mod {6}".format(
                    base, d, r, 2 ** r, d * (2 ** r), result, prime_candidate
                )
            )
            if result == -1 or (result - prime_candidate == -1):
                printer("        Passed so it can be a prime")
                encountered_solution = True
                break
            printer("        Failed so we continue checking")
        if not encountered_solution:
            printer(
                "      Check of all r values by base {} resulted in failure, {} is not a prime".format(
                    base, prime_candidate
                )
            )
            return False
    return True


def run_test_suite():
    test_miller_rabin_with_explanation(197, [7, 11], True, default_printer)
    print(
        "[Further function calls will not print commentary text to stdout as sideeffect]"
    )
    test_miller_rabin_with_explanation(243, [12, 14], False, null_printer)
    test_miller_rabin_with_explanation(567, [7, 5], False, null_printer)
    test_miller_rabin_with_explanation(397, [2, 3], True, null_printer)


def test_miller_rabin_with_explanation(
    prime_candidate, numbers_to_test, expected, printer
):
    print("-" * 80)
    print(
        "CASE prime_candidate = {}, testnumbers={}".format(
            prime_candidate, str(numbers_to_test)
        )
    )
    actual = miller_rabin_with_explanation(
        prime_candidate, numbers_to_test, printer=printer
    )
    result_str = "PASS" if expected == actual else "FAIL"
    print("[{}] expected {} got {}".format(result_str, expected, actual))


def main():
    run_test_suite()


##############################################################################

if __name__ == "__main__":
    main()
