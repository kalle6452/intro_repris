def pascal_line(n):
    # Base case
    if n == 0:
        return [[1]]
    else:
        # Our current row, it will always start with one.
        current = [1]
        # Recursive step
        answer = pascal_line(n-1)
        # Previous row is one above our current one.
        prev = answer[-1]
        # 
        for i in range(len(prev)-1):
            current.append(prev[i] + prev[i+1])
        current += [1]
        answer.append(current)
    return answer


def pascal_rec(n):
    return pascal_line(n)


print(pascal_rec(2))


