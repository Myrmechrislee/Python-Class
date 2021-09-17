import numpy as n, time

rankings = []
def test_state(i):
    seq = []
    state = i
    while seq[-2:] != [2, 1]:
        if state % 2 == 1:
            state = (3 * state + 1) / 2
        else:
            state = state / 2
        seq.append(state)
    rankings.append((i, len(seq)))

for i in range(1, int(1e+6)):
    test_state(i)

rankings.sort(key=lambda x: x[1], reverse=True)

print("State\tSequences")
for i in rankings[:10]:
    print(i[0], "\t", i[1])
