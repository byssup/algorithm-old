
MOD = 20091101


def solve(nums, k):
    pnums = [0 for _ in range(len(nums) + 1)]
    for i, num in enumerate(nums):
        pnums[i + 1] = pnums[i] + num
    return '%s %s' % (int(solve_by_partialsum(pnums, k)), solve_by_dp(nums, pnums, k))


def solve_by_partialsum(pnums, k):
    count = [0 for _ in range(len(pnums))]
    for pnum in pnums:
        count[pnum % k] += 1

    res = 0
    for c in count:
        if c >= 2:
            res = ((res + (c * (c - 1)) / 2) % MOD)
    return res


def solve_by_dp(nums, pnums, k):
    pass


if __name__ == '__main__':
    for _ in range(int(input())):
        arr = input().split()
        k = int(arr[1])
        nums = [int(num) for num in input().split()]
        print(solve(nums, k))