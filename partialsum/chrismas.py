

MOD = 20091101


def solve(nums, k):
    psum = [0 for _ in range(len(nums) + 1)]
    for i, num in enumerate(nums):
        psum[i + 1] = psum[i] + num
    count = [0 for _ in range(len(nums) + 1)]
    for ps in psum:
        count[ps % k] += 1
    res = 0
    for c in count:
        if c >= 2:
            res += (c * (c - 1) / 2) % MOD
    return res

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        arr = raw_input().split()
        _, k = arr[0], int(arr[1])
        nums = [int(num) for num in raw_input().split()]    
        print solve(nums, k)