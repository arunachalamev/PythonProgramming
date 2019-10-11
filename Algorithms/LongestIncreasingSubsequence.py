
def longest_increasing_subsequence(x):
    counter = [1]*len(x)

    for i in range(len(x)):
        for j in range(i):
            if x[j]<x[i]:
                counter [i] = max(counter[i],counter[j]+1)


    return counter


if __name__ == "__main__":
    x = [10,9,2,5,3,7,101,180]
    print(max(longest_increasing_subsequence(x)))

