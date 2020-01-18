

def letterCombinations(digits):
    mapping = { "1":  "",
                "2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz"
    }

    def backtrack(combination,digits):
        if len(digits) == 0:
            output.append(combination)
        else:
            for ch in mapping[digits[0]]:
                backtrack(combination+ch,digits[1:])



    output = []
    backtrack("",digits)
    return output


def letterCombinations2(digits):
    mapping = { "1":  "",
                "2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz"
    }
    all_combinations = list(mapping[digits[0]])
    for d in digits[1:]:
        current_combination = []
        for ch in mapping[d]:
            for comb in all_combinations:
                current_combination.append(comb+ch)
        all_combinations = current_combination
    
    return all_combinations


print (letterCombinations("23"))
print (letterCombinations2("23"))
