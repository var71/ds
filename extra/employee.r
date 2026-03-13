# the employee aptitude and job score are as follows
Aptitude : 85,65,50,68,87,74,65,96,68,94,73,84,85,97,91 
Job Scores : 70,90,80,89,88,86,78,67,86,90,92,94,99,93,87 
refer chi square test to study the co relation between aptitude and job score proficiency of employees formulate the null and alternative hypothesis , interpret the result

aptitude <- c(85,65,50,68,87,74,65,96,68,94,73,84,85,97,91)
jobscore <- c(70,90,80,89,88,86,78,67,86,90,92,94,99,93,87)

# Categorize scores (High >= 80, Low < 80)
apt_cat <- ifelse(aptitude >= 80, "High", "Low")
job_cat <- ifelse(jobscore >= 80, "High", "Low")

# Create contingency table
table_data <- table(apt_cat, job_cat)

# Perform Chi-square test
chisq.test(table_data)
