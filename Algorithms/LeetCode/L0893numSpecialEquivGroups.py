

def numSpecialEquivGroups(A):
    def count(A):
        ans = [0] * 52
        for i, letter in enumerate(A):
            ans[ord(letter) - ord('a') + 26 * (i%2)] += 1
        return tuple(ans)

    return len({count(word) for word in A})


print(numSpecialEquivGroups(["abcd","cdab","cbad","xyzz","zzxy","zzyx"]))