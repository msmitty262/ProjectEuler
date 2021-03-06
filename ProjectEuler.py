import numpy as np
import pandas as pd

### #1 Multiple of 3 and 5 ###

# Slow, methodical method

def number1():
    num1 = 3
    num2 = 5
    maximum = 1000
    result = 0
    for i in range(maximum):
        if (i % num1 == 0) | (i % num2 == 0):
            result += i
    return result

# Much faster method

def number1alt():
    num1 = 3
    num2 = 5
    maximum = 1000
    num3 = num1 * num2
    maximum = maximum - 1
    n1 = num1 * (int(maximum / num1) * (int(maximum / num1) + 1)) / 2
    n2 = num2 * (int(maximum / num2) * (int(maximum / num2) + 1)) / 2
    n3 = num3 * (int(maximum / num3) * (int(maximum / num3) + 1)) / 2
    return int(n1 + n2 - n3)

### #2 Even Fibonacci numbers ###

def number2():
    n = 4000000
    fib = [1, 2]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    del fib[-1]
    a = 0
    for i in fib:
        if i % 2 == 0:
            a += i
    return a

#3 Largest prime factor

def is_prime(n):
    a = int(np.sqrt(n)) + 1
    nums = range(2,a)
    if all(n % num != 0 for num in nums):
        b = 1
    else:
        b = 0
    return b

def number3():
    n = 600851475143
    a = int(np.sqrt(n)) + 1
    for i in range(a):
        if n % (a-i) == 0:
            if is_prime(a - i) == 1:
                return (a - i)
                break

### #4 Largest Palindrome product ###

def number4():
    na = 100
    nb = 1000
    big_list = {}

    for a in range(na, nb):
        for b in range(na, nb):
            prod = a * b
            if str(prod)[0] == str(prod)[len(str(prod)) - 1]:
                if str(prod)[1] == str(prod)[len(str(prod)) - 2]:
                    if str(prod)[2] == str(prod)[len(str(prod)) - 3]:
                        big_list[(a,b)] = a * b
                    else:
                        big_list[(a,b)] = 0
                else:
                    big_list[(a,b)] = 0
            else:
                big_list[(a,b)] = 0

    maximum = max(big_list.values())
    return(maximum)

### #5 Smallest multiple ###

def number5():
    n = 20
    nums = range(1, n + 1)
    b = n
    c = 0
    while c == 0:
        if all(b % num == 0 for num in nums):
            c = 1
        b += n
    return b - n
    
### #6 Sum square difference ###

def number6():
    n = 100
    numbers = range(1, n + 1)
    a = sum(n**2 for n in numbers)
    b = (sum(n for n in numbers)) ** 2
    c = b - a
    return c

### #7 10001st prime ###
    
def number7():
    n = 10001
    primes = [2]
    attempt = 3
    while len(primes) < n:
        if all(attempt % prime != 0 for prime in primes):
            primes.append(attempt)
        attempt += 2
    return primes[-1]

### #8 Largest product in a series ###

def number8():
    n = 13
    big = []
    w1 = 731671765313306249192251196744265747423553491949349698352031277450632623957831801698480186947885184385861560789112949495459501737958331952853208805511
    w2 = 125406987471585238630507156932909632952274430435576689664895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749
    w3 = 303589072962904915604407723907138105158593079608667017242712188399879790879227492190169972088809377665727333001053367881220235421809751254540594752243
    w4 = 525849077116705560136048395864467063244157221553975369781797784617406495514929086256932197846862248283972241375657056057490261407972968652414535100474
    w5 = 821663704844031998900088952434506585412275886668811642717147992444292823086346567481391912316282458617866458359124566529476545682848912883142607690042
    w6 = 2421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    what = str(w1) + str(w2) + str(w3) + str(w4) + str(w5) + str(w6)
    
    for i in range(1000 - n + 1):
        num = int(what[i:i+n])
        prod = 1
        while(num != 0):
            prod = prod * (num % 10)
            num = int(num/10)
        big.append(prod)
    big.sort()
    return big[-1]

    
### #9 Special Pythagorean triplet ###
    
def number9():
    n = 1000
    big = []
    for a in range(1,n):
        for b in range(1,n-a):
            c = n - a - b
            if (c**2 == a**2 + b**2) & (a+b+c == n):
                z = a*b*c
                big.append(z)
    return big[0]

### #10 Summation of primes ###

def number10():
    n = 2000000
    primes = [2]
    a = int(np.sqrt(n)) + 1
    for i in range(2, a):
        if all(i % prime != 0 for prime in primes):
            primes.append(i)
    primes2 = primes.copy()
    for i in range(a,n):
        if all(i % prime != 0 for prime in primes2):
            primes.append(i)
    sum1 = sum(primes)
    return sum1

### #11 Largest product in a grid ###
    
def number11():
    w1 = pd.Series([8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8])
    w2 = pd.Series([49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0])
    w3 = pd.Series([81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65])
    w4 = pd.Series([52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91])
    w5 = pd.Series([22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80])
    w6 = pd.Series([24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50])
    w7 = pd.Series([32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70])
    w8 = pd.Series([67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21])
    w9 = pd.Series([24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72])
    w10 = pd.Series([21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95])
    w11 = pd.Series([78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92])
    w12 = pd.Series([16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57])
    w13 = pd.Series([86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58])
    w14 = pd.Series([19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40])
    w15 = pd.Series([4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66])
    w16 = pd.Series([88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69])
    w17 = pd.Series([4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36])
    w18 = pd.Series([20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16])
    w19 = pd.Series([20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54])
    w20 = pd.Series([1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48])
    df = pd.concat([w1, w2, w3,w4,w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16, w17, w18, w19, w20], axis = 1)
    df = df.T
    horizontal = []
    for row in range(20):
        for col in range(17):
            prod = df.at[row, col] * df.at[row, col + 1] * df.at[row, col + 2] * df.at[row, col + 3]
            horizontal.append(prod)
    vertical = []
    for row in range(17):
        for col in range(20):
            prod = df.at[row, col] * df.at[row + 1, col] * df.at[row + 2, col] * df.at[row + 3, col]
            vertical.append(prod)
    diagnol_down = []
    for row in range(17):
        for col in range(17):
            prod = prod = df.at[row, col] * df.at[row + 1, col + 1] * df.at[row + 2, col + 2] * df.at[row + 3, col + 3]
            diagnol_down.append(prod)
    diagnol_up = []
    for row in range(17):
        for col in range(17):
            prod = prod = df.at[row + 3, col] * df.at[row + 2, col + 1] * df.at[row + 1, col + 2] * df.at[row, col + 3]
            diagnol_up.append(prod)
    max1 = max(horizontal)
    max2 = max(vertical)
    max3 = max(diagnol_down)
    max4 = max(diagnol_up)
    maximum = max(max1, max2, max3, max4)
    return(maximum)

### #13 Large Sum ###

def number13():
    n1 = pd.Series([37107287533902102798797998220837590246510135740250, 46376937677490009712648124896970078050417018260538, 74324986199524741059474233309513058123726617309629, 91942213363574161572522430563301811072406154908250])
    n2 = pd.Series([23067588207539346171171980310421047513778063246676, 89261670696623633820136378418383684178734361726757, 28112879812849979408065481931592621691275889832738, 44274228917432520321923589422876796487670272189318])
    n3 = pd.Series([47451445736001306439091167216856844588711603153276, 70386486105843025439939619828917593665686757934951, 62176457141856560629502157223196586755079324193331, 64906352462741904929101432445813822663347944758178])
    n4 = pd.Series([92575867718337217661963751590579239728245598838407, 58203565325359399008402633568948830189458628227828, 80181199384826282014278194139940567587151170094390, 35398664372827112653829987240784473053190104293586])
    n5 = pd.Series([86515506006295864861532075273371959191420517255829, 71693888707715466499115593487603532921714970056938, 54370070576826684624621495650076471787294438377604, 53282654108756828443191190634694037855217779295145])
    n6 = pd.Series([36123272525000296071075082563815656710885258350721, 45876576172410976447339110607218265236877223636045, 17423706905851860660448207621209813287860733969412, 81142660418086830619328460811191061556940512689692])
    n7 = pd.Series([51934325451728388641918047049293215058642563049483, 62467221648435076201727918039944693004732956340691, 15732444386908125794514089057706229429197107928209, 55037687525678773091862540744969844508330393682126])
    n8 = pd.Series([18336384825330154686196124348767681297534375946515, 80386287592878490201521685554828717201219257766954, 78182833757993103614740356856449095527097864797581, 16726320100436897842553539920931837441497806860984])
    n9 = pd.Series([48403098129077791799088218795327364475675590848030, 87086987551392711854517078544161852424320693150332, 59959406895756536782107074926966537676326235447210, 69793950679652694742597709739166693763042633987085])
    n10 = pd.Series([41052684708299085211399427365734116182760315001271, 65378607361501080857009149939512557028198746004375, 35829035317434717326932123578154982629742552737307, 94953759765105305946966067683156574377167401875275])
    n11 = pd.Series([88902802571733229619176668713819931811048770190271, 25267680276078003013678680992525463401061632866526, 36270218540497705585629946580636237993140746255962, 24074486908231174977792365466257246923322810917141])
    n12 = pd.Series([91430288197103288597806669760892938638285025333403, 34413065578016127815921815005561868836468420090470, 23053081172816430487623791969842487255036638784583, 11487696932154902810424020138335124462181441773470])
    n13 = pd.Series([63783299490636259666498587618221225225512486764533, 67720186971698544312419572409913959008952310058822, 95548255300263520781532296796249481641953868218774, 76085327132285723110424803456124867697064507995236])
    n14 = pd.Series([37774242535411291684276865538926205024910326572967, 23701913275725675285653248258265463092207058596522, 29798860272258331913126375147341994889534765745501, 18495701454879288984856827726077713721403798879715])
    n15 = pd.Series([38298203783031473527721580348144513491373226651381, 34829543829199918180278916522431027392251122869539, 40957953066405232632538044100059654939159879593635, 29746152185502371307642255121183693803580388584903])
    n16 = pd.Series([41698116222072977186158236678424689157993532961922, 62467957194401269043877107275048102390895523597457, 23189706772547915061505504953922979530901129967519, 86188088225875314529584099251203829009407770775672])
    n17 = pd.Series([11306739708304724483816533873502340845647058077308, 82959174767140363198008187129011875491310547126581, 97623331044818386269515456334926366572897563400500, 42846280183517070527831839425882145521227251250327])
    n18 = pd.Series([55121603546981200581762165212827652751691296897789, 32238195734329339946437501907836945765883352399886, 75506164965184775180738168837861091527357929701337, 62177842752192623401942399639168044983993173312731])
    n19 = pd.Series([32924185707147349566916674687634660915035914677504, 99518671430235219628894890102423325116913619626622, 73267460800591547471830798392868535206946944540724, 76841822524674417161514036427982273348055556214818])
    n20 = pd.Series([97142617910342598647204516893989422179826088076852, 87783646182799346313767754307809363333018982642090, 10848802521674670883215120185883543223812876952786, 71329612474782464538636993009049310363619763878039])
    n21 = pd.Series([62184073572399794223406235393808339651327408011116, 66627891981488087797941876876144230030984490851411, 60661826293682836764744779239180335110989069790714, 85786944089552990653640447425576083659976645795096])
    n22 = pd.Series([66024396409905389607120198219976047599490197230297, 64913982680032973156037120041377903785566085089252, 16730939319872750275468906903707539413042652315011, 94809377245048795150954100921645863754710598436791])
    n23 = pd.Series([78639167021187492431995700641917969777599028300699, 15368713711936614952811305876380278410754449733078, 40789923115535562561142322423255033685442488917353, 44889911501440648020369068063960672322193204149535])
    n24 = pd.Series([41503128880339536053299340368006977710650566631954, 81234880673210146739058568557934581403627822703280, 82616570773948327592232845941706525094512325230608, 22918802058777319719839450180888072429661980811197])
    n25 = pd.Series([77158542502016545090413245809786882778948721859617, 72107838435069186155435662884062257473692284509516, 20849603980134001723930671666823555245252804609722, 53503534226472524250874054075591789781264330331690])
    df = pd.DataFrame([n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17, n18, n19, n20, n21, n22, n23, n24, n25])
    a = df.iloc[:,0].sum()
    b = df.iloc[:,1].sum()
    c = df.iloc[:,2].sum()
    d = df.iloc[:,3].sum()
    e = a + b + c + d
    e = str(e)
    return e[:10]

### #14 Longest Collatz Sequence ###

def problem14():
    num = 1000000
    lengths = []
    for i in range(0,num):
        a = [i]
        while i > 1:
            if i % 2 == 0:
                i = i / 2
                a.append(i)
            else:
                i = 3 * i + 1
                a.append(i)
        length = len(a)
        lengths.append(length)
    lengths = np.array(lengths)
    where = np.where(lengths == max(lengths))
    return where

### #15 Lattice Paths
    
def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res = res * i
    return res

def problem15():
    num = 20
    a = int(factorial(num * 2))
    b = int(factorial(num) ** 2)
    c = int(a // b)
    return c

### #16 Power digit sum ###
    
def problem16():
    num = 1000
    a = 2 ** num
    a = str(a)
    b = len(a)
    c = 0
    for i in range(b):
        d = int(a[i])
        c += d
    return c

### #17 Number letter counts

def problem17():
    n1 = len('one') * (90 + 100 + 1)
    n2 = len('two') * (90 + 100)
    n3 = len('three') * (90 + 100)
    n4 = len('four') * (90 + 100)
    n5 = len('five') * (90 + 100)
    n6 = len('six') * (90 + 100)
    n7 = len('seven') * (90 + 100)
    n8 = len('eight') * (90 + 100)
    n9 = len('nine') * (90 + 100)
    n10 = len('ten') * 10
    n11 = len('eleven') * 10
    n12 = len('twelve') * 10
    n13 = len('thirteen') * 10
    n14 = len('fourteen') * 10
    n15 = len('fifteen') * 10
    n16 = len('sixteen') * 10
    n17 = len('seventeen') * 10
    n18 = len('eighteen') * 10
    n19 = len('nineteen') * 10
    n20 = len('twenty') * 100
    n30 = len('thirty') * 100
    n40 = len('forty') * 100
    n50 = len('fifty') * 100
    n60 = len('sixty') * 100
    n70 = len('seventy') * 100
    n80 = len('eighty') * 100
    n90 = len('ninety') * 100
    hund = len('hundred') * 100 * 9
    nand = len('and') * 99 * 9
    thous = len('thousand')
    singles = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9
    teens = n11 + n12 + n13 + n14 + n15 + n16 + n17 + n18 + n19
    tens = n10 + n20 + n30 + n40 + n50 + n60 + n70 + n80 + n90
    result = singles + teens + tens + hund + nand + thous
    return result

### #20 Factorial digit sum

def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res = res * i
    return res

def number20():
    num = 100
    a = factorial(num)
    a = str(a)
    b = len(a)
    c = 0
    for i in range(b):
        d = int(a[i])
        c += d
    return c

### #74 Digit factorial change

def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res = res * i
    return res

def number74():
    num = 1000000
    big = []
    for i in range(1, num):
        g = [i]
        repeat = []
        for f in range(60):
            if len(g) == 1:
                z = str(g[0])
            else:
                z = str(g[-1])
            a = len(z)
            e = 0
            for b in range(a):
                c = int(z[b])
                d = factorial(c)
                e += d
            if all(t != e for t in g):
                g.append(e)
            else:
                repeat.append(f)
                break
        big.append(repeat[0] + 1)
    counter = big.count(60)
    return counter

### #100 Arranged probability

def number100():
    num = 10 ** 12
    blue = [15]
    tot = [21]
    while tot[-1] < num:
        a = 3 * blue[-1] + 2 * tot[-1] - 2
        b = 4 * blue[-1] + 3 * tot[-1] - 3
        blue.append(a)
        tot.append(b)
    result = blue[-1]
    return result

### #111 Primes with runs

def get_numbers(num, size, runs):
    a = np.ones(size) * num
    m = []
    if runs == 1:
        for b in range(size):
            for c in range(10):
                d = a.copy()
                d[b] = c
                if c != num:
                    e = 0
                    for i in range(size):
                        f = d[i] * 10 ** (size - i)
                        e +=f
                    m.append(e // 10)
    if runs == 2:
        for b in range(size - 1):
            for c in range(10):
                for g in range(b + 1, size):
                    for h in range(10):
                        d = a.copy()
                        d[b] = c
                        d[g] = h
                        if c != num and h != num:
                            e = 0
                            for i in range(size):
                                f = d[i] * 10 ** (size - i)
                                e +=f
                            m.append(e // 10)
    
    return m

def get_prime_factors(n):
    primes = [2]
    a = int(np.sqrt(n)) + 1
    for i in range(2, a):
        if all(i % prime != 0 for prime in primes):
            primes.append(i)
    return primes

def number111():
    digits = 10
    num = 10 ** digits
    primes = get_prime_factors(num)
    c = 0
    for i in range(10):
        numbers = get_numbers(i, digits, 1)
        a = []
        for number in numbers:
            if all(number % prime != 0 for prime in primes):
                if number > num // 10:
                    a.append(number)
        if len(a) == 0:
            numbers = get_numbers(i, digits, 2)
            a = []
            for number in numbers:
                if all(number % prime != 0 for prime in primes):
                    if number > num // 10:
                        a.append(number)
        b = sum(a)
        c += b
        
    return int(c)
