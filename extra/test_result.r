#By seeing the poor performance of students in first class test , remedial lectures were arranged by the department ,
#department is claiming that after remedial lectures performance improved ,. 
#The test result for both before and after is given . 
Test 1 = 85 ,68 , 67 , 84 , 98 , 60 , 94 , 80 , 94, 98,95,80,85,87,75 
Test 2 = 70,90,80,89,88,86,78,87,90,86,92,94,99,93,86 
apply paired t test to determine if there is a significant difference in the test score


test1 <- c(85,68,67,84,98,60,94,80,94,98,95,80,85,87,75)

test2 <- c(70,90,80,89,88,86,78,87,90,86,92,94,99,93,86)

t.test(test1, test2, paired = TRUE, alternative = "two.sided")
