def First():
    hours_worked = [26, 17, 31, 40, 18, 23, 21, 22, 14, 21, 39, 34, 10, 27, 31, 11, 22, 10, 10, 24]
    pay_rates = [16.35, 24.35, 16.97, 22.9, 24.54, 19.45, 19.51, 16.28, 17.17, 22.82, 20.89, 24.88, 23.43, 15.9, 21.22, 20.19, 24.74, 17.87, 17.24, 18.11]

    print(len(hours_worked))
    print(len(pay_rates))

    ans = []
    for i in range(len(hours_worked)):
        ans.append(hours_worked[i] * pay_rates[i])

    print(ans)

# Payment to Employee = Hourly Pay Rate * Num Hours Work * 0.9 (10% tax payment) - 100 (Benefits)
def Second():
    Hours_Worked = [45, 76, 78, 59, 70, 78, 76, 76, 77, 48, 63, 72, 68, 51, 58, 76, 46, 47, 70, 68, 47, 50, 66, 58, 43, 74]
    Pay_Rate = 15.75
    Actual_Pay = [537.875, 1197.0, 1228.5, 736.325, 1102.5, 1228.5, 1197.0, 1197.0, 991.4750000000001, 756.0, 793.025, 1134.0, 1071.0, 622.9250000000001, 913.5, 1197.0, 724.5, 566.225, 1102.5, 1071.0, 566.225, 787.5, 1039.5, 913.5, 509.525, 1165.5]

    ans = []
    for i in range(len(Hours_Worked)):
        print(f'Actual Pay: {Actual_Pay[i]}, Expected {(Pay_Rate * Hours_Worked[i] * 0.9 - 100)}')
        ans.append(Actual_Pay[i] - (Pay_Rate * Hours_Worked[i] * 0.9 - 100))
    print(sum(ans))

def Third():
    phrase1 = "You've blue tried the rest; now try blue the blue best.  The A1A Car Wash is the best in town.  Founded by Bogdan blue Walynetz, it's now family blue owned blue by the blue Walter blue White blue Family.  blue With his blue expertise in science, blue he's taken this car wash to blue a new and blue better blue level.  blue Make sure to blue come on blue by for blue an A1 day."
    phrase2 = "this is blue a blue test"
    print(len(str.replace(phrase1, "blue ", "")))

def Fourth():
    ans = ''
    text = 'V xabj jung lbh qvq... Urvfraoret.'
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for c in text:
        if str.isalpha(c):
            idx = alpha.index(str.upper(c)) - 13
            if idx < 0:
                idx += len(alpha)
            if c.isupper():
                ans += alpha[idx]
            else:
                ans += alpha[idx].lower()
        else:
            ans += c
    print(ans)
Fourth()