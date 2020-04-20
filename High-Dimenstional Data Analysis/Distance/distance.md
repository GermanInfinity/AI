In this lesson, we learn how to compute the distance between samples in a 
high dimensional data set using R. The formula we learn is the sum of 
sqaures distance and the data we work on is the RNA expression levels for 
seven tissues, each with several biologicaal replicates.

Notes:
Number of biological replicates for hippocampus: 31
 
Distance between samples 3 and 45: 152.5662
Takes the difference between each entry in samples in question, squares and 
takes the sum, and then the square root. (R: dist function does this))
Must transpose rows to columns to compute distance between samples.

Distance between gene 214086_at and 200805_at:

Distance between all pairs of samples: 17766 
