s = input()

alphabet = [-1] * 26

for i in range(len(s)):
    if alphabet[ord(s[i]) - ord('a')] == -1:
        alphabet[ord(s[i]) - ord('a')] = i

for i in alphabet:
    print(i,end=" ")