class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)

        d, r = deque(), deque()

        for i, c in enumerate(senate):
            if c == "R":
                r.append(i)
            else:
                d.append(i)
        
        while d and r:
            d_turn = d.popleft()
            r_turn = r.popleft()

            if r_turn < d_turn:
                r.append(d_turn + len(senate))
            else:
                d.append(r_turn + len(senate))
        
        return "Radiant" if r else "Dire"