library(tissuesGeneExpression) 
data(tissuesGeneExpression)
set.seed(1)
ind <- sample(nrow(e), 500)
Y <- t(apply(e[ind,],1,scale)) #Standardize col
s <- svd(Y)
U <- s$u
V <- s$v
D <- diag(s$d)
Yhat <- U%*% D %*% t(V)
resid <- Y - Yhat
max(abs(resid))
dim(e)
# Now reduce dimensions
