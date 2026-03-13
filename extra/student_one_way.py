# Class A = List(85,90,88,82,87) Class B= List(76,78,80,81,75) Class C=List(92,88,94,89,90) Consider a dataset that contains the exam score of studnets of 3 class A , B and C perform one way anova test using python or r to determine if there is a significant difference in the mean exam score among these classes , formulate the null and alternative hypothesis

from scipy.stats import f_oneway

# Scores of each class
class_A = [85, 90, 88, 82, 87]
class_B = [76, 78, 80, 81, 75]
class_C = [92, 88, 94, 89, 90]

# Perform One-Way ANOVA
F_statistic, p_value = f_oneway(class_A, class_B, class_C)

print("F Statistic:", F_statistic)
print("P Value:", p_value)

# Decision
alpha = 0.05
if p_value < alpha:
    print("Reject Null Hypothesis: Significant difference exists")
else:
    print("Fail to Reject Null Hypothesis: No significant difference")
