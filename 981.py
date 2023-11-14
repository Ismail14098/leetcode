class TimeMap:
    m = defaultdict(list)

    def __init__(self):
        self.m = defaultdict(list)
    
    def findPos(self, key: str, timestamp: int) -> int:
        values = self.m[key]
        l, r = 0, len(values)-1
        result = r
        while l <= r and l < len(values) and r >= 0:
            m = (l+r)//2
            value, time = values[m]
            if time > timestamp:
                r = m-1
            else:
                result = m
                l = m+1
        return result

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.m[key]
        if len(values) == 0:
            return ""

        value, time = values[self.findPos(key, timestamp)]
        if time > timestamp:
            return ""
        return value