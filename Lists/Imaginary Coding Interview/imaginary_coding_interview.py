def interview(times, max_time):
    if len(times) == 8 and times[0] <= VERY_EASY and times[1] <= VERY_EASY and times[2] <= EASY and times[3] <= EASY and times[4] <= MEDIUM and times[5] <= MEDIUM and times[6] <= HARD and times[7] <= HARD and max_time <= INTERVIEW:
        return 'qualified'
    return 'disqualified'


VERY_EASY = 5
EASY = 10
MEDIUM = 15
HARD = 20
INTERVIEW = 120

print(interview([5, 5, 10, 10, 15, 15, 20, 20], 120))
print(interview([2, 3, 8, 6, 5, 12, 10, 18], 64))
print(interview([5, 5, 10, 10, 25, 15, 20, 20], 120))
print(interview([5, 5, 10, 10, 15, 15, 20], 120))
print(interview([5, 5, 10, 10, 15, 15, 20, 20], 130))
