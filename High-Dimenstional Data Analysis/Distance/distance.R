library(tissuesGeneExpression)
data(tissuesGeneExpression)
head(e)
tail(e)
head(tissue)

d <- dist(t(e))
as.matrix(d)[3,45] #Distance between samples
length(d) #Length of data sample

image(as.matrix(d)) #Image of distances