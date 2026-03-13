this is my excel file 
A B C 
85 76 92 
90 78 88 
88 80 94 
82 81 89
87 75 90 


satlevel <- read.csv(file.choose(), header = TRUE)

# Convert wide format to long format
scores <- stack(satlevel)

# Rename columns
colnames(scores) <- c("Score", "Class")

# Perform One Way ANOVA
anovatable <- aov(Score ~ Class, data = scores)

summary(anovatable)
