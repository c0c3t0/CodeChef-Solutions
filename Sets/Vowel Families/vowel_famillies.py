def same_vowel_group(words):
    vowels = {'a', 'o', 'u', 'e', 'i'}
    first_word_volews = vowels.intersection(set(words[0]))
    result = []

    for w in words:
        if first_word_volews == vowels.intersection(set(w)):
            result.append(w)

    return result


print(same_vowel_group(['toe', 'ocelot', 'maniac']))
print(same_vowel_group(["many", "carriage", "emit", "apricot", "animal"]))
print(same_vowel_group(["hoops", "chuff", "bot", "bottom"]))

# same_vowel_group(["toe", "ocelot", "maniac"]) ➞ ["toe", "ocelot"]

# same_vowel_group(["many", "carriage", "emit", "apricot", "animal"]) ➞ ["many"]

# same_vowel_group(["hoops", "chuff", "bot", "bottom"]) ➞ ["hoops", "bot", "bottom"]
