library(SimComp)
library(plyr)

file <- system.file(file='../all_variants_annotated_merged.csv')

main.dataset <- read.csv(file)

benign.dataset <- subset(main.dataset, simplified.significance==c('1/10k', 'benign'))

len.ben <- length(benign.dataset$foldx.ddg)
mean.ben <- mean(benign.dataset$foldx.ddg)
sd.ben <- sd(benign.dataset$foldx.ddg)

generated.values <- rnorm(len.ben, mean=mean.ben, sd= sd.ben)
gen <- main.dataset

for(i in 1:nrow(gen)){
  if(is.na(gen$foldx.ddg[i])==TRUE){
    if(gen$simplified.significance[i]=='benign'){
      gen$foldx.ddg[i] <- sample(generated.values, 1)
    }
      if(gen$simplified.significance[i]=='1/10k'){
        gen$foldx.ddg[i] <- sample(generated.values, 1)    
      }
    }
  }

  
write.csv(file="Simulated_foldx_benign.csv", x = gen)