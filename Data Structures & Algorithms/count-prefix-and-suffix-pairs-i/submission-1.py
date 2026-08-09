class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def is_prefix(w1, w2):
            return w1 == w2[:len(w1)]

        def is_suffix(w1, w2):
            return w1 == w2[len(w2) - len(w1):]

        counter = 0
        
        for w1 in range(len(words)):
            for w2 in range(w1 + 1, len(words)):
                if is_prefix(words[w1], words[w2]) and is_suffix(words[w1], words[w2]):
                    counter += 1
        
        return counter