def factorial(n):
    total = 1
    for i in range(1, n+1):
        total = total * i
    return total

def sum(*number):
    total = 0
    for i in number:
        total += i
    return total

def fibinachi(n):
    past = 0
    now = 1
    result = [past, now]
    for i in range(0, n+1):
        present = now + past
        past = now
        now = present
        result.append(now)
    return result

# print(sum(1,2,3))
# print(factorial(6))

print(fibinachi(5))

