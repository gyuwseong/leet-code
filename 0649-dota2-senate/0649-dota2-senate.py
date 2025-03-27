class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        global s
        if len(senate) < 2:
            s = senate[0]
        else:
            q = collections.deque(senate)

            while len(q) > 1:
                s = q.popleft()
                for i in range(len(q)):
                    if s != q[i]:
                        del q[i]
                        q.append(s)
                        break

        if s == "R":
            return "Radiant"
        else:
            return "Dire"