"""Does this sentence match the pattern."""
import sys


def get_permutations(pattern_matches, sentence, pattern):
    if not sentence and not pattern:
        return True
    if not pattern and sentence:
        return False
    if pattern and not sentence:
        return False
    is_match = False

    current_letter = pattern[0]
    if(current_letter in pattern_matches):
        symbol_match = pattern_matches.get(current_letter)
        if(sentence[0:len(symbol_match)]
                == symbol_match):
            return (get_permutations(dict(pattern_matches),
                    sentence[len(symbol_match):], pattern[1:]))
        else:
            return False

    for x in xrange(0, len(sentence)):
        current_letter = pattern[0]
        pattern_matches[current_letter] = sentence[0:x + 1]
        is_match = (get_permutations(dict(pattern_matches),
                    sentence[x + 1:], pattern[1:]))
        if is_match:
            return True
    return is_match

print get_permutations({}, sys.argv[1], sys.argv[2])
