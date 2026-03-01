import numpy as np

np.random.seed(42)

scores = np.random.randint(50, 101, size=(5, 4))

print("Scores:\n", scores)
print("\n3rd student, 2nd subject:", scores[2, 1])
print("\nLast 2 students:\n", scores[-2:, :])
print("\nFirst 3 students, subjects 2 & 3:\n", scores[:3, 1:3])


column_mean = np.round(scores.mean(axis=0), 2)
print("\nColumn-wise mean:", column_mean)
curve = np.array([5, 3, 7, 2])
curved_scores = scores + curve
curved_scores = np.clip(curved_scores, 0, 100)
print("\nCurved Scores:\n", curved_scores)
row_max = curved_scores.max(axis=1)
print("\nRow-wise max:", row_max)

row_min = curved_scores.min(axis=1, keepdims=True)
row_max = curved_scores.max(axis=1, keepdims=True)

normalized = (curved_scores - row_min) / (row_max - row_min)
max_index = np.unravel_index(np.argmax(normalized), normalized.shape)

print("Student index:", max_index[0])
print("Subject index:", max_index[1])

high_scores = curved_scores[curved_scores > 90]
print("\nScores above 90:", high_scores)
