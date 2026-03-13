scores <- read.csv(file.choose(), header=TRUE)

anova_result <- aov(score ~ class, data=scores)

summary(anova_result)


dataset=# Scores of each class
class_A = [85, 90, 88, 82, 87]
class_B = [76, 78, 80, 81, 75]
class_C = [92, 88, 94, 89, 90]
