cryptogram = 'beafraidanddoitanyway'
s = list(cryptogram)

for i in range(25):
    answer = []
    for j in range(len(s)):
        decrypt = chr((ord(s[j]) - ord('a') + i) % 26 + ord('a'))
        answer.append(decrypt)
    print(''.join(answer))