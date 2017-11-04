def solve(i, s):
    j = i
    tree = ['', '', '', '']
    k = 0
    head = ''
    while j < len(s) and k < 4:
        if s[j] == 'x':
            head = 'x'
            tree[k] = solve(j + 1, s)
        else:
            tree[k] = s[j]
        j += len(tree[k])
        k += 1
    return head + tree[2] + tree[3] + tree[0] + tree[1]


if __name__ == '__main__':
    for _ in range(int(raw_input())):
        print solve(0, raw_input())
