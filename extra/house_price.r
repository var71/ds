# Sample dataset
data <- data.frame(
  Area = c(1000,1500,2000,2500,3000),
  Bedrooms = c(2,3,3,4,4),
  Age = c(10,5,3,2,1),
  Price = c(200000,300000,400000,500000,600000)
)

# Train model
model <- lm(Price ~ Area + Bedrooms + Age, data=data)

# View model summary
summary(model)

# Predict new house price
new_house <- data.frame(Area=2200, Bedrooms=3, Age=5)
predict(model, new_house)
