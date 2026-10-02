T = int(input())
for t in range(T):
    lst = list(map(int, input().split()))

    ans = round(sum(lst)/len(lst))

    print(f"#{t+1} {ans}")