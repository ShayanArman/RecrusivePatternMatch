from StateMachine import PatternMatching as MatchPattern

match_pattern = MatchPattern()
is_matched = match_pattern.get_permutations({}, "dogcatliondoglionb", "abcacd")
print is_matched
