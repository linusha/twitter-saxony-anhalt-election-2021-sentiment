data$isEmotional = ifelse(data$sentiment > 0, 1, 0)
data$isPositive = ifelse(data$polarity > 0, 1, 0)
data$isNegative = ifelse(data$polarity < 0, 1, 0)
data$isMixed = ifelse(data$polarity == 0 & data$isEmotional, 1, 0)

data$isEmotional_liwc = ifelse(data$total_liwc_sentiment > 0, 1, 0)
data$isPositive_liwc = ifelse(data$negemo < data$posemo, 1, 0)
data$isNegative_liwc = ifelse(data$negemo > data$posemo, 1, 0)
data$isMixed_liwc = ifelse(data$negemo == data$posemo & data$isEmotional_liwc, 1, 0)

top_50_stats <- data %>% 
  group_by(author_name) %>% 
  dplyr::summarize(retweet_sum = sum(retweet_count), 
                   emotional_sum_ss = sum(isEmotional),
                   positive_sum_ss = sum(isPositive),
                   negative_sum_ss = sum(isNegative),
                   mixed_sum_ss = sum(isMixed),
                   emotional_sum_liwc = sum(isEmotional_liwc),
                   positive_sum_liwc = sum(isPositive_liwc),
                   negative_sum_liwc = sum(isNegative_liwc),
                   mixed_sum_liwc = sum(isMixed_liwc),
                   n = n()) %>%
  dplyr::arrange(desc(retweet_sum)) %>%
  slice_head(n = 50) %>%
  summarise(across(where(is.numeric), ~ sum(., is.na(.), 0)))


user = data %>% 
  group_by(author_name) %>%
  summarise(avg=mean(author_follower_count))

mean(user$avg)

median(user$avg)