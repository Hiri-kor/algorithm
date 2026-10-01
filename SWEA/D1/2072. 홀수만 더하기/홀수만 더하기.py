T = int(input())
for t in range(T):
    numbers = list(map(int, input().split()))
    ans = 0
    for number in numbers:
        if number % 2 == 1:
            ans += number

    print(f"#{t+1} {ans}")