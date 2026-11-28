print("=" * 32 + "\nROTATE MY SCORES\n" + "=" * 32)

scores = [10, 20, 30, 40, 50]
print("\nPART 1: Two-Pointer Swap")
print("Original Scores:", scores)
print("Reversed Scores:", scores[::-1])

scores = [1, 2, 3, 4, 5, 6, 7, 8]
k = 3
print("\nPART 2: Reverse in Groups")
print(f"Original Scores: {scores} | Group Size: {k}")
grouped = [x for i in range(0, len(scores), k) for x in scores[i : i + k][::-1]]
print("Scores After Group Reverse:", grouped)

scores = [10, 20, 30, 40, 50]
print("\nPART 3: Left Rotate by 1")
print("Original Scores:", scores)
print("After Left Rotate by 1:", scores[1:] + scores[:1])

scores = [10, 20, 30, 40, 50, 60]
n = 2
print("\nPART 4: Left Rotate by n")
print(f"Original Scores: {scores} | n: {n}")
n %= len(scores) # made case if it's larger than n
print(f"After Left Rotate by {n}:", scores[n:] + scores[:n])

scores = [16, 17, 4, 3, 5, 2]
print("\nPART 5: Leaders in an Array")
print("Original Scores:", scores)
leaders = [s for i, s in enumerate(scores) if s > max(scores[i + 1 :], default=-1)]
print("Leaders:", leaders)