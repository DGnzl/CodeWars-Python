from typing import ByteString
from requests.api import request


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
# Fourth()

def Fifth():
    import json
    with open('a1a_financials.json','r') as file:
        data = json.load(file)
    ans = [x['date'] for x in data if x['profit'] - (x['num_washes'] * 15) > 5000]
    print(f"flag{','.join(ans)}")
# Fifth()

def Nemo_1():
    input = 'Emmanuel,Cameron,Gracie,Taylor,Aliyah,Cayden,Brady,Henry,Londyn,Emily,Nemo,Eden,Lucas,Jack,Lincoln,Everett,Mya,Sean,Easton,Jaxson'.split(',')
    start = 7
    print(input.index('Nemo'))
# Nemo_1()

def Nemo_2():
    clue1 = 'Y2FsaWZvcm5pYSBhZHZlbnR1cmU6IGluY3JlZGktY29hc3RlciAxNDIy'
    clue2 = 'qPbqr o19'
    print(len(clue1))

def Nemo_3():
    nums = [1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,
    10946,17711,28657,46368,75025,121393,196418,317811,514229,832040,1346269,
    2178309,3524578,5702887,9227465,14930352,24157817,39088169,63245986,
    102334155,165580141,267914296,433494437,701408733,1134903170,1836311903,
    2971215073,4807526976,7778742049,12586269025,20365011074,32951280099,
    53316291173,86267571272,139583862445,225851433717,365435296162,591286729879,
    956722026041,1548008755920,2504730781961,4052739537881,6557470319842,
    10610209857723,17167680177565,27777890035288,44945570212853,72723460248141,
    117669030460994,190392490709135,308061521170129,498454011879264,
    806515533049393,1304969544928657,2111485077978050,3416454622906707,
    5527939700884757,8944394323791464,14472334024676221,23416728348467685,
    37889062373143906,61305790721611591,99194853094755497,160500643816367088,
    259695496911122585,420196140727489673,679891637638612258,1100087778366101931,
    1779979416004714189,2880067194370816120,4660046610375530309,7540113804746346429,
    12200160415121876738,19740274219868223167,31940434634990099905,51680708854858323072,
    83621143489848422977,135301852344706746049,218922995834555169026,354224848179261915075]
    ans = [x % 25672 for x in nums]
    print(ans)
# Nemo_3()
def Nemo_4():
    with open('peter_pan_ch1.txt', 'r') as file:
        input = file.read().lower()
    idx = 0
    total = 0
    while input.find('peter',idx) != -1:
        total += input.index('peter',idx)
        idx = min(input.index('peter',idx) + 1, len(input) - 1)
    print(total)
# Nemo_4()

def Nemo_5():
    import random
    fib_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 
    1597, 2584, 4181, 6765, 10946, 17711, 2985, 20696, 23681, 18705, 16714, 9747, 
    789, 10536, 11325, 21861, 7514, 3703, 11217, 14920, 465, 15385, 15850, 5563, 
    21413, 1304, 22717, 24021, 21066, 19415, 14809, 8552, 23361, 6241, 3930, 10171, 
    14101, 24272, 12701, 11301, 24002, 9631, 7961, 17592, 25553, 17473, 17354, 9155, 
    837, 9992, 10829, 20821, 5978, 1127, 7105, 8232, 15337, 23569, 13234, 11131, 
    24365, 9824, 8517, 18341, 1186, 19527, 20713, 14568, 9609, 24177, 8114, 6619, 
    14733, 21352, 10413, 6093, 16506, 22599, 13433, 10360, 23793, 8481, 6602, 15083]
    random.seed(102274)
    nemo_id = random.choice(fib_list)
    import json
    with open('customer_id_log.json','r') as j_file:
        cust_id = json.load(j_file)
    nemo_hash = cust_id[nemo_id]['id']
    print(nemo_hash)
# Nemo_5()

import requests
def Moira_2():
    api_url = 'http://ctf.kronoskoders.com:8888/moria/inside'
    response = requests.get(api_url)
    cubes = [x ** 3 for x in range(100)]
    #print(cubes)
    closing = response.content.index(b'}') + 1
    print(closing)
    for x in cubes:
        if x < closing:
            print(chr(response.content[x]), end='')
# Moira_2()

def Moira_3():
    api_url = 'http://ctf.kronoskoders.com:8888/moria/door/open'
    todo = {'Friend': 'mellon'}
    response = requests.post(api_url, json=todo)
    print(response.json())
    print(response.status_code)

def Moria_5():
    api_url = 'http://ctf.kronoskoders.com:8888/moria/bridge'
    todo = {"username":"Bot"}
    response = requests.post(api_url, json=todo)
    print(response.text)
    print(response.status_code)
Moria_5()