# ------------------------------------------------------------------------------
# Clear workspace
# ------------------------------------------------------------------------------
rm(list = ls())


# ------------------------------------------------------------------------------
# Load libraries
# ------------------------------------------------------------------------------
#install.packages("tidyverse")
library("tidyverse")
library(dplyr)
# ------------------------------------------------------------------------------
# Load data
# ------------------------------------------------------------------------------

my_url <- "https://www.ncbi.nlm.nih.gov/Class/FieldGuide/BLOSUM62.txt" 
bl62 <- read_table(file = my_url,  col_names = TRUE,  comment = "#") 
bl62 <- column_to_rownames(bl62, var = "X1")
write_tsv(x = bl62,
          path = "data/bl62.csv")
my_data_l <- read_csv(file = "data/all_variants_annotated_merged.csv")
my_data_l <- as_tibble(my_data_l)

Gran <- read_csv(file = "data/Grantham.dist.matrix.csv")
Gran <- column_to_rownames(Gran, var = "X1")

Gran["S"] <- 0
Gran["B"] <- 0
Gran["Z"] <- 0
Gran["X"] <- 0
Gran["*"] <- 0
Gran <- rbind(Gran, "B" = 0)
Gran <- rbind(Gran, "Z" = 0)
Gran <- rbind(Gran, "X" = 0)
Gran <- rbind(Gran, "*" = 0)
Gran <- rbind(Gran, "W" = 0)

# ------------------------------------------------------------------------------
# AA substitution vs .ddg
# ------------------------------------------------------------------------------
res<-c()
my_diag <- (bl62[my_data_l$AA.mut,my_data_l$AA.wt])
for (i in 1:dim(my_diag)[1]){
  res[i]<-my_diag[i,i]
}
my_data_l <- my_data_l %>% 
  mutate('BL62_subs' = res)

res2<-c()
my_diag2 <- (Gran[my_data_l$AA.mut ,my_data_l$AA.wt])
for (i in 1:dim(my_diag2)[1]){
  res2[i]<-my_diag2[i,i]
}
my_data_l <- my_data_l %>% 
  mutate('Gran_subs' = res2)
colnames(Gran)
Gran <- Gran %>% 
  mutate('S' = 0)

