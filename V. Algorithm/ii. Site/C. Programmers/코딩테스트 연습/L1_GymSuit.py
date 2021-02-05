# 2020-03-30-Mon

# Try 1 8/12

def solution(n, lost, reserve):
    students = dict()
    # check clothes for each student
    for i in range(n):
        students[str(i)] = 1
        if i in lost:
            students[str(i)] -= 1
        if i in reserve:
            students[str(i)] += 1
    # borrow
    clothes = students
    for i in range(n):
        # only can check after
        if i == 0:
            # lost
            if students[str(i)] == 0:
                # can borrow
                if students[str(i+1)] == 2:
                    clothes[str(i)] += 1
                    students[str(i+1)] -= 1
                # can't borrow
                else:
                    clothes[str(i)] == 0
            # didn't loss
            else:
                clothes[str(i)] == 1
        # only can check before
        elif i == n-1:
            # lost
            if students[str(i)] == 0:
                # can borrow
                if students[str(i-1)] == 2:
                    clothes[str(i)] += 1
                    students[str(i-1)] -= 1
                # can't borrow
                else:
                    clothes[str(i)] == 0
            # didn't loss
            else:
                pass
                # clothes[str(i)] == 1
        # can compare with before and after number
        else:
            # lost
            if students[str(i)] == 0:
                if students[str(i-1)] == 2:
                    clothes[str(i)] += 1
                    students[str(i-1)] -= 1
                elif students[str(i+1)] == 2:
                    clothes[str(i)] += 1
                    students[str(i+1)] -= 1
                else:
                    pass
                    # clothes[str(i)] == 0
            # didn't loss
            else:
                pass
                # clothes[str(i)] == 1
    # Count students who have clothes
    count = 0
    for i in range(n):
        if clothes[str(i)] >= 1:
            count += 1
        else:
            pass
    return count

#  Try 2 8/12

def solution(n, lost, reserve):
    students = dict()
    # check clothes for each student
    for i in range(n):
        students[str(i)] = 1
        if i in lost:
            students[str(i)] -= 1
        if i in reserve:
            students[str(i)] += 1
    # borrow
    clothes = students
    for i in range(n):
        # only can check after
        if i == 0:
            # lost
            if students[str(i)] == 0:
                # can borrow
                if students[str(i+1)] == 2:
                    students[str(i)] += 1 # clothes[str(i)] += 1
                    students[str(i+1)] -= 1
                # can't borrow
                else:
                    pass
                    # clothes[str(i)] == 0
            # didn't loss
            else:
                pass
                # clothes[str(i)] == 1
        # only can check before
        elif i == n-1:
            # lost
            if students[str(i)] == 0:
                # can borrow
                if students[str(i-1)] == 2:
                    students[str(i)] += 1# clothes[str(i)] += 1
                    students[str(i-1)] -= 1
                # can't borrow
                else:
                    pass
                    # clothes[str(i)] == 0
            # didn't loss
            else:
                pass
                # clothes[str(i)] == 1
        # can compare with before and after number
        else:
            # lost
            if students[str(i)] == 0:
                if students[str(i-1)] == 2:
                    students[str(i)] += 1# clothes[str(i)] += 1
                    students[str(i-1)] -= 1
                elif students[str(i+1)] == 2:
                    students[str(i)] += 1# clothes[str(i)] += 1
                    students[str(i+1)] -= 1
                else:
                    pass
                    # clothes[str(i)] == 0
            # didn't loss
            else:
                pass
                # clothes[str(i)] == 1
    # Count students who have clothes
    count = 0
    for i in range(n):
        if students[str(i)] >= 1:
        # if clothes[str(i)] >= 1:
            count += 1
        else:
            pass
    return count

# Try 3 25% 런타임에러

def solution(n, lost, reserve):
    students = dict()
    # check clothes for each student
    for i in range(1, n+1):
        students[str(i)] = 1
        if i in lost:
            students[str(i)] -= 1
        if i in reserve:
            students[str(i)] += 1
    print(students)
    # borrow
    clothes = students
    for i in range(1, n+1):
        # only can check after
        if i == 0:
            # lost
            if students[str(i)] == 0:
                # can borrow
                if students[str(i+1)] == 2:
                    students[str(i)] += 1 # clothes[str(i)] += 1
                    students[str(i+1)] -= 1
                # can't borrow
                else:
                    pass
                    # clothes[str(i)] == 0
            # didn't loss
            else:
                pass
                # clothes[str(i)] == 1
        # only can check before
        elif i == n-1:
            # lost
            if students[str(i)] == 0:
                # can borrow
                if students[str(i-1)] == 2:
                    students[str(i)] += 1# clothes[str(i)] += 1
                    students[str(i-1)] -= 1
                # can't borrow
                else:
                    pass
                    # clothes[str(i)] == 0
            # didn't loss
            else:
                pass
                # clothes[str(i)] == 1
        # can compare with before and after number
        else:
            # lost
            if students[str(i)] == 0:
                if students[str(i-1)] == 2:
                    students[str(i)] += 1# clothes[str(i)] += 1
                    students[str(i-1)] -= 1
                elif students[str(i+1)] == 2:
                    students[str(i)] += 1# clothes[str(i)] += 1
                    students[str(i+1)] -= 1
                else:
                    pass
                    # clothes[str(i)] == 0
            # didn't loss
            else:
                pass
                # clothes[str(i)] == 1
    # Count students who have clothes
    count = 0
    for i in range(1, n+1):
        if students[str(i)] >= 1:
        # if clothes[str(i)] >= 1:
            count += 1
        else:
            pass
    print(students)
    return count

# Try 4 100%

def solution(n, lost, reserve):
    students = dict()
    # check clothes for each student
    for i in range(1, n+1):
        students[str(i)] = 1
        if i in lost:
            students[str(i)] -= 1
        if i in reserve:
            students[str(i)] += 1
    print(students)
    # borrow
    clothes = students
    for i in range(1, n+1):
        # only can check after
        if i == 1:
            # lost
            if students[str(i)] == 0:
                # can borrow
                if students[str(i+1)] == 2:
                    students[str(i)] += 1 # clothes[str(i)] += 1
                    students[str(i+1)] -= 1
                # can't borrow
                else:
                    pass
                    # clothes[str(i)] == 0
            # didn't loss
            else:
                pass
                # clothes[str(i)] == 1
        # only can check before
        elif i == n:
            # lost
            if students[str(i)] == 0:
                # can borrow
                if students[str(i-1)] == 2:
                    students[str(i)] += 1# clothes[str(i)] += 1
                    students[str(i-1)] -= 1
                # can't borrow
                else:
                    pass
                    # clothes[str(i)] == 0
            # didn't loss
            else:
                pass
                # clothes[str(i)] == 1
        # can compare with before and after number
        else:
            # lost
            if students[str(i)] == 0:
                if students[str(i-1)] == 2:
                    students[str(i)] += 1# clothes[str(i)] += 1
                    students[str(i-1)] -= 1
                elif students[str(i+1)] == 2:
                    students[str(i)] += 1# clothes[str(i)] += 1
                    students[str(i+1)] -= 1
                else:
                    pass
                    # clothes[str(i)] == 0
            # didn't loss
            else:
                pass
                # clothes[str(i)] == 1
    # Count students who have clothes
    count = 0
    for i in range(1, n+1):
        if students[str(i)] >= 1:
        # if clothes[str(i)] >= 1:
            count += 1
        else:
            pass
    print(students)
    return count
