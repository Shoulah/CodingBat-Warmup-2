""" def string_times(str, n):
    if n >= 0:
        return str * n


print(string_times("ah", 3)) """

""" def front_times(str, n):
    if len(str) < 3:
        return n * str
    else:
        return str[0:3] * n

print(front_times("Ahmed", 2)) 
print(front_times("Shoulah", 3))
print(front_times("ah", 3))   """     

""" 
def string_bits(str):
    if len(str) == 1:
        return str
    else:
        result = ""
        i = 0
        while i < len(str):
            if i % 2 == 0:
                result += str[i]
            i += 1
        return result

print(string_bits("Shoulah"))            
 """

def string_splosion(str):
    if len(str) > 0:
        result = ""
        i = 1
        while i <= len(str):
            result += str[0:i]
            i += 1
        return result

print(string_splosion("Code"))        
