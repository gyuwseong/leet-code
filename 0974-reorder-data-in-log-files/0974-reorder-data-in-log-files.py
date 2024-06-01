class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits, letters = [], []
        for st in logs:
            if st.split()[1].isdigit():
                digits.append(st)
            else:
                letters.append(st)
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits
        