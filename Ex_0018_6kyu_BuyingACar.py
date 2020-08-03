def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    # your code
    savings = 0
    num_month = 0
    # percentLossByMonth = percentLossByMonth - 0.5
    while startPriceNew > startPriceOld + savings:
        num_month += 1
        percentLossByMonth = percentLossByMonth + 0.5 * ((num_month + 1) % 2)
        savings += savingperMonth
        startPriceNew = startPriceNew * (1 - percentLossByMonth/100)
        startPriceOld = startPriceOld * (1 - percentLossByMonth/100)
    return [num_month, round(startPriceOld + savings - startPriceNew)]


if __name__ == '__main__':
    # percentLossByMonth = 1.5-0.5
    # num_month = 0
    # for i in range(7):
    #     percentLossByMonth = percentLossByMonth + 0.5 * ((num_month + 1) % 2)
    #     num_month += 1
    #     print(f"{i}: {percentLossByMonth}")

    print(nbMonths(2000, 8000, 1000, 1.5))
    print(nbMonths(2000, 8000, 1000, 1.5))