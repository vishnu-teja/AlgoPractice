file = open("./course_2/week_3/median.txt", "r")

nums = {}
targets = {}

for line in map(int, file.readlines()):
    nums[str(line)] = int(line)

# nums = {"22": 22, "54": 54, "121212": 121212}


for i in range(-10000, 10000):
    for n in nums:
        ot = i - nums[n]
        if ot != nums[n] and str(ot) in nums:
            targets[str(i)] = i


print(len(targets))
