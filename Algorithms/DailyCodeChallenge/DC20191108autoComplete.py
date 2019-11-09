def add_to_trie(s, trie):
    if not s:
        return trie

    character = s[0]
    if character not in trie:
        trie[character] = dict()
    
    # recursively call trie data structure
    trie[character] = add_to_trie(s[1:], trie[character])

    return trie

def get_dictionary_trie(dictionary):
    trie = dict()
    # add each word to a trie data structure
    for word in dictionary:
        trie = add_to_trie(word, trie)

    return trie

def get_possible_completions(trie):
    possible_completions = list()
    for character in trie:
        if trie[character]:
            child_completions = get_possible_completions(trie[character])
            for child_completion in child_completions:
                possible_completions.append(character + child_completion)
        else:
            possible_completions.append(character)
        
    return possible_completions

def get_autocomplete_suggestions(s, dictionary):
    # create a trie data structure
    trie = get_dictionary_trie(dictionary)

    current_trie = trie
    # get the trie for the corresponding prefix
    for character in s:
        if character not in current_trie:
            return []
        current_trie = current_trie[character]

    #from trie get the list of string
    completions = get_possible_completions(current_trie)
    completions = [s + x for x in completions]

    return completions 

assert get_autocomplete_suggestions("de", ["dog", "deer", "deal"]) == ["deer", "deal"]
assert get_autocomplete_suggestions("ca", ["cat", "car", "cer"]) == ["cat", "car"]
assert get_autocomplete_suggestions("ae", ["cat", "car", "cer"]) == []
assert get_autocomplete_suggestions("ae", []) == []