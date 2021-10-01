def solution(n, times):
    sorted(times)
    # small, big, answer
    s, b = 1, n * times[-1]
    answer = b
    while s <= b:
        mid = (s + b) // 2
        tot = 0
        for time in times:
            tot += mid // time
        if tot < n:
            s = mid + 1
        else:
            if mid <= answer:
                answer = mid
            b = mid - 1
    return answer
