def fact_fraction(n, a):# n*(n-1) * ...  * (n - a + 1) / a!
    tot = 1
    for i in range(a):
        tot*= n + i + 1
        tot//= i + 1
    return tot

def arrangements(dict):
    total = 1
    sum = 0
    for char in dict:
        total *= fact_fraction(sum, dict[char])
        sum += dict[char]
    return total

def listPosition(word):
    sortedword = [char for char in word]
    sortedword.sort()
    val = {}
    reps = {}
    counter = 0
    for char in sortedword:
        if not(char in val):
            val[char] = counter
            counter += 1
            reps[char] = 1
        else:
            reps[char] += 1
    l = len(word)
    counter = 1
    for i in range(l):
        is_smaller = True
        for char in val:
            if is_smaller:
                if char != word[i]:
                    if reps[char] > 0:
                        reps[char]-= 1
                        counter += arrangements(reps)
                        reps[char] += 1
                        #count how many words start with word[:i-1] + char and are anagrams of word
                        #this is equal to n! / prod reps[i]!
                else:
                    is_smaller = False
                    #set up new val and reps
                    reps[word[i]] -= 1
    """
    for each char in word
        find how many words can start with a hip_char smaller than char
    """
    return counter
