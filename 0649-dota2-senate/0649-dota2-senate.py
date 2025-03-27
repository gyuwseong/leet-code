class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        start = len(senate)
        radiant = collections.deque()
        dire = collections.deque()

        for i, s in enumerate(senate):
            if s == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                radiant.append(r + start)
            else:
                dire.append(d + start)

        return "Radiant" if radiant else "Dire"