import time
''' This function compressed the given string.
 We first iterate through all the char value in a String and comprane the current char with the previous char.'''
def compress(s):
    compressed = ""
    cnt = 1
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            cnt += 1
        else:
            compressed = compressed + s[i - 1]
            if cnt > 1:
                compressed += str(cnt)
            cnt = 1
    compressed = compressed + s[-1]
    if cnt > 1:
        compressed += str(cnt)
    return compressed

s = "abbbaaaaaaccdaaab"
start_time = time.time()
compress(s)
print('Execution time:',time.time() - start_time  , 'seconds')

# Although the time difference is insighnificant the complexity of the code is O(n) because we iterate through the string. 
