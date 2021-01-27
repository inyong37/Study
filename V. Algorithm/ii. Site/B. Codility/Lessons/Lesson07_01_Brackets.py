# 50% https://app.codility.com/demo/results/trainingA3DAV4-KY9/

def solution(S):
    if len(S) == 0:
        return 1
    elif len(S) % 2 != 0:
        return 0
    else:
        result_a = 0 # (
        result_b = 0 # {
        result_c = 0 # [
        
        for i in S:
            if i == '(':
                result_a += 1
            elif i == ')':
                result_a -= 1
            elif i == '[':
                if result_a > 0:
                    return 0
                else:
                    result_b += 1
            elif i == ']':
                if result_a > 0:
                    return 0
                else:
                    result_b -= 1
            elif i == '{':
                if result_a > 0 or result_b > 0:
                    return 0
                else:
                    result_c += 1
            else:
                if result_a > 0 or result_b > 0:
                    return 0
                else:
                    result_c -= 1
            
            if result_a < 0 or result_b < 0 or result_c < 0:

# 100% https://app.codility.com/demo/results/trainingURVSB3-7PZ/

def solution(S):
    if len(S) == 0:
        return 1
    elif len(S) % 2 != 0:
        return 0
    else:
        count = 0
        stack = []
        for i in S:
            if i == '{' or i == '[' or i =='(':
                # stack.push()
                stack.append(i)
            # elif i == '}' or i ==']' or i ==')':
            else:
                if len(stack) == 0:
                    return 0
                else:
                    bracket = stack.pop()
                    if bracket == '{':
                        if i != '}':
                            return 0
                    elif bracket == '[':
                        if i != ']':
                            return 0
                    else:
                        if i != ')':
                            return 0
        if len(stack) > 0:
            return 0
        return 1
            
                return 0
            
            # print(result_a, result_b, result_c)
        
        if result_a != 0 or result_b != 0 or result_c != 0:
            return 0
        return 1
