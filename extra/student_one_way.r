scores <- read.csv(file.choose(), header=TRUE)

anova_result <- aov(score ~ class, data=scores)

summary(anova_result)
