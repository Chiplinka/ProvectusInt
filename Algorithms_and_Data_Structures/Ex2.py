#   Time complexity O(n) - linear because we have only 1 for loop from 0 to end of string
#   Space: O(m) - also linear we used n for input string and also m for saving data about characters we have in string
#   in worst case it is of size of alphabet

s = "absgss"
d = {}
ans = 0
i = 0
for j in range(len(s)):
    if s[j] in d:
        i = max(i, d[s[j]] + 1)
    d[s[j]] = j
    ans = max(ans, j-i + 1)
print(ans)