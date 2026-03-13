#consider a scenario where you have test scores from a sample of students and you want to compare the mean of 
#this mean with score with hypothesis population mean 
#Apply one sample t test using python or r ,
#assume hypothesis mean = 70 , formulate the null and alternate hypothesis interpret 
#the result and conclusion 72,88,64,74,67,79,85,75,89,77 one sample t test karna hai


scores <- c(72,88,64,74,67,79,85,75,89,77)

t.test(scores, mu = 70, alternative = "two.sided")
