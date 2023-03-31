def generate_hashtag(s):
    ans = "#"
    for w in s.split(" "):
        ans += w.capitalize()
    if len(ans) > 140 or ans == "#" :
        return False
    return ans
    #your code here
    pass
