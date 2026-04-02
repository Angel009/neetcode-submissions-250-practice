class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for s in strs:
            s_len = str(len(s))
            encoded.append(s_len + "#" + s)
        
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            s_len = int(s[i:j])
            decoded.append(s[j + 1:j + 1 + s_len])

            i = j + 1 + s_len

        return decoded


