#perform linear regresiion on iris dataset on petal length and petal width

data(iris)

model <- lm(Petal.Width ~ Petal.Length, data = iris)

summary(model)
