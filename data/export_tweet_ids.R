library(here)
load(here('prod.RData'))
tweet_ids <- data$id
write.table(tweet_ids, '~/tweet_ids.txt', append = FALSE, sep = "\n", dec = ".",
            row.names = FALSE, col.names = FALSE)