#perform linear regression on following dataset for predicting the salary of his / her depending on years of experience
My csv file is 
Years 2 , 10 , 4 , 20 ,8 , 12 , 22 
Salary 30000 , 95000,45000,78000,84000,120000,200000

salarydata <- read.csv(file.choose(), header = TRUE)

model <- lm(Salary ~ Years, data = salarydata)

summary(model)
