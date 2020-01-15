""" def string_times(str, n):
    if n >= 0:
        return str * n


print(string_times("ah", 3)) """

def front_times(str, n):
    if len(str) < 3:
        return n * str
    else:
        return str[0:3] * n

print(front_times("Ahmed", 2)) 
print(front_times("Shoulah", 3))
print(front_times("ah", 3))       