class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 1
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars = sorted(cars)

        time = []
        for p, s in cars:
            time.append((target - p) / s)

        time.reverse()
        max = time[0]
        for t in time:
            if t > max:
                fleets += 1
                max = t

        return fleets