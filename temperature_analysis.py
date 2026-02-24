import numpy as np
import time

temps_celsius = np.array([22, 25, 28, 24, 26])
temps_fahrenheit = temps_celsius * 1.8 + 32
average_fahrenheit = round(np.mean(temps_fahrenheit), 1)

print("Celsius:", temps_celsius)
print("Fahrenheit:", temps_fahrenheit)
print("Average Fahrenheit:", average_fahrenheit)
#-----------------------------------------------------------#
test_scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])
highest_score = np.max(test_scores)
lowest_score = np.min(test_scores)
score_range = highest_score - lowest_score

print("Shape:", test_scores.shape)
print("Total elements:", test_scores.size)
print("Highest score:", highest_score)
print("Lowest score:", lowest_score)
print("Range:", score_range)
#-----------------------------------------------------------#
np_arr = np.arange(1, 50001);
list_arr = list(range(1, 50001));

np_start = time.time();
np_sum = np.sum(np_arr);
np_end = time.time();

list_start = time.time();
list_sum = sum(list_arr);
list_end = time.time();

np_time = np_end - np_start;
list_time = list_end - list_start;

speed_ratio = round(list_time/np_time,1);

print("NumPy sum:", np_sum)
print("Python sum:", list_sum)
print("NumPy time:", format(np_time, ".4f"), "seconds")
print("Python time:", format(list_time, ".4f"), "seconds")
print(f"NumPy is {speed_ratio}x faster")
