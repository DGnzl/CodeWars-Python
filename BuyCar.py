def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    months = 0
    savings = 0
    while (savings + startPriceOld < startPriceNew):
        months += 1
        savings += savingperMonth
        startPriceOld *= ((100 - percentLossByMonth) / 100)
        startPriceNew *= ((100 - percentLossByMonth) / 100)
        if months % 2 != 0:
            percentLossByMonth += 0.5
    return [months, round(savings + startPriceOld - startPriceNew)]

print(nbMonths(2000, 8000, 1000, 1.5)) # 6, 766
print(nbMonths(12000, 8000, 1000, 1.5)) # 0, 4000