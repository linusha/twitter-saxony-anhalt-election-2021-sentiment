# FIRST STEP
# export tweets to run senti strength
data <- read.csv('data.csv')
tweets <- data$processed_text
write.csv(tweets,'tweet_text.csv')

# Run SentiStrength Analysis

# SECOND STEP
# add senti strength data and derived features to data set
data <- read.csv('data.csv')
sentiment_data <- read.csv('tweet_text0_out.txt', sep="\t")

sentiment_data$polarity <- sentiment_data$Positive + sentiment_data$Negative
sentiment_data$sentiment <- (sentiment_data$Positive - sentiment_data$Negative) - 2
sentiment_data$is_Negative <- sentiment_data$polarity < 0
sentiment_data$interaction_term <- sentiment_data$sentiment * sentiment_data$is_Negative

sentiment_data$Text <- NULL
data <- cbind(data, sentiment_data)
write.csv(data, 'final_dataset.csv')
save(data, file = 'final_dataset.RData')



