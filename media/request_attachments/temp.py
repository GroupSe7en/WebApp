n = int(input())
for i in range(n):
    b = int(input().split()[1])
    price_arr = list(map(int, input().split()))
    tot = 0
    count = 0
    while b > tot:
        price = min(price_arr)
        if (tot + price <= b):
            tot += price
            price_arr.remove(price)
            count += 1
        else:
            break
    print("Case #" + str(i) + ": " + str(count))
