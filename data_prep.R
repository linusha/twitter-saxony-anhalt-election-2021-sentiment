###############################
######  PLEASE IGNORE #########
###############################

# otherwise log transformation fails
# data <- data[data$author_follower_count > 0,]
# TODO: fixme and put in a nice place
# save(data, file = here('prod.RData'))
#export in csv
# write.csv2(data, file="C:/Users/Olga/Desktop/data9894.csv")


# subsample of all tweets that are retweetet at least once in order to
# check assumptions/statistics on this subsample as well
# data_subset_retweeted <- data[data$retweet_count > 0,]

# data$liwc_polarity <- data$posemo - data$negemo
# data$liwc_isNegative <- ifelse(data$liwc_polarity < 0, 1, 0)
# data$liwc_interaction_term <- data$liwc_isNegative * data$total_liwc_sentiment

# # merge with liwc data
# liwc_data <- read.csv(here('liwc.csv'))
# data <- cbind(data, liwc_data)
# data$negemo <- gsub(",",".", data$negemo)
# data$posemo <- gsub(",", ".", data$posemo)
# data$negemo <- as.numeric(data$negemo)
# data$posemo <- as.numeric(data$posemo)
# data$total_liwc_sentiment <- data$negemo + data$posemo
# save(data, file= here('prod.RData'))
# data$Tone <- gsub(",", ".", data$Tone)
# data$Tone <- as.numeric(data$Tone)
# data$author_verified <- ifelse(data$author_verified == "True", TRUE, FALSE)
# data$is_Negative <- as.numeric(data$is_Negative)
# data$author_verified <- as.numeric(data$author_verified)

