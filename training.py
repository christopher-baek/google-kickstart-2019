def hours(p, s, start, end):
    if s[start] == s[end]:
        return 0

    hours = 0

    for i in range(start, end):
        hours += s[end] - s[i]

    return hours


def solve(n, p, s):
    """
    - 1 <= Si <= 10000
    - 2 <= p <= n
    - team is fair if it has exactly p students on it
      and they have all the same skill rating
    - takes student one hour of coaching to increase
      the skill rating of any student by 1
    """
    s.sort()

    min_so_far = float('inf')

    for i in range(n - p + 1):
        h = hours(p, s, i, i + p - 1)
        if h == 0:
            return 0

        if h < min_so_far:
            min_so_far = h

    return min_so_far


def main():
    """
    - 1 <= t <= 100
    """
    t = int(input())

    for test_case_index in range(t):
        n_and_p = input()
        n_and_p = n_and_p.split(' ')
        n = int(n_and_p[0])
        p = int(n_and_p[1])
        s = [int(s) for s in input().split(' ')]
        print('Case #{}: {}'.format(test_case_index + 1, solve(n, p, s)))


if __name__ == '__main__':
    main()
