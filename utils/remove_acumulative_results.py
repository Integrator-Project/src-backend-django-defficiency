def remove_acumulative_results(list_base):
    inverted = list_base.copy()[::-1]
    list_base.clear()
    for previous, current in zip(inverted, inverted[1:]):
        p_value, p_date = previous
        c_value, c_date = current

        result = abs(p_value - c_value)
        list_base.append((result, p_date))

    list_base.reverse()
