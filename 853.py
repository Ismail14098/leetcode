class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
            cars = []
            for i in range(len(position)):
                cars.append((position[i], speed[i]))
            cars = sorted(cars, reverse=True)
            result = []
            for car in cars:
                if len(result) == 0:
                    result.append(car)
                    continue
                leadPos, leadSpeed = result.pop()
                leadSteps = (target-leadPos)/leadSpeed
                carSteps = (target-car[0])/car[1]
                if carSteps <= leadSteps:
                    result.append((leadPos, leadSpeed))
                else:
                    result.append((leadPos, leadSpeed))
                    result.append(car)
            return len(result)

# improvemets:
# * compact cars population
# * in result store seconds
# * compare last two and if faster pop()

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
            cars = [(p, s) for p, s in zip(position, speed)]
            cars = sorted(cars, reverse=True)
            result = []
            for car in cars:
                result.append((target-car[0])/car[1])
                if len(result) >= 2 and result[-1] <= result[-2]:
                    result.pop()
            return len(result)