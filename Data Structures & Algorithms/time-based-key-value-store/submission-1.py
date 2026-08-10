class TimeMap:

    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = []
        self.storage[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        val = self.storage.get(key, [])
        l, r = 0, len(val) - 1
        while l <= r:
            mid = (l + r) // 2
            if val[mid][1] <= timestamp:
                result = val[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return result