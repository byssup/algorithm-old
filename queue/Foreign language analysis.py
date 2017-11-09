class NumberFactory():
    def __init__(self):
        self.num = 1983

    def create_num(self):
        self.num = (self.num * 214013 + 2531011)
        return self.num % 10000 + 1


def solve(N, K):
    number_factory = NumberFactory()
    queue = []
    count = 0
    range_sum = 0
    head = 0

    for _ in range(K + 1):

        num = number_factory.create_num()
        queue.append(num)
        range_sum += num

        while queue and range_sum > N:
            range_sum -= queue[head]
            head += 1

        if head >= 100000:
            queue = queue[head:]
            head = 0

        if range_sum == N:
            count += 1

    return count


if __name__ == '__main__':
    for _ in range(int(raw_input())):
        arr = raw_input().split()
        print solve(int(arr[0]), int(arr[1]))
