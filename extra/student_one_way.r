classA <- c(85,90,88,82,87)
classB <- c(76,78,80,81,75)
classC <- c(92,88,94,89,90)

scores <- c(classA, classB, classC)
group <- factor(rep(c("A","B","C"), each=5))

anova_result <- aov(scores ~ group)

summary(anova_result)
