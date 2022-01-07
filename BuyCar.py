def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    months = 0
    savings = 0
    while (savings + startPriceOld < startPriceNew):
        months += 1
        savings += savingperMonth
    return [savings + startPriceOld - startPriceNew]

print(nbMonths(2000, 8000, 1000, 1.5)) # 6, 766