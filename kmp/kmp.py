

def get_slow_pi(n):
    m = len(n)
    pi = [0 for _ in range(m)]
    for begin in range(1, m):
        for i in range(m - begin):
            if n[begin + i] != n[i]:
                break
            pi[begin + i] = max(pi[begin + i], i + 1)
    return pi


def get_fast_pi(n):
    m = len(n)
    pi = [0 for _ in range(m)]
    matched = 0
    begin = 1
    while begin + matched < m:
        if n[begin + matched] == n[matched]:
            matched += 1
            pi[begin + matched - 1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return pi

