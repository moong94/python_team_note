import sys

word = sys.stdin.readline().strip()

word = word.replace("c=", "1")
word = word.replace("c-", "1")
word = word.replace("dz=", "1")
word = word.replace("d-", "1")
word = word.replace("lj", "1")
word = word.replace("nj", "1")
word = word.replace("s=", "1")
word = word.replace("z=", "1")

print(len(word))
