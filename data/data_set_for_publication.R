# Only some columns are relevant/allowed to be kept.
# All Data relevant for the modelling/most important summary statistics are staying.
# Some descriptives (information about the authors of tweets) are gone.
load('prod.RData')
columns_to_keep <- c("retweet_count",
                     "reply_count",
                     "like_count",
                     "quote_count",
                     "author_follower_count",
                     "retweet_timelag",
                     "hashtag_count",
                     "url_existence",
                     "user_activity", 
                     "Positive",
                     "Negative",
                     "polarity",
                     "sentiment",
                     "is_Negative",
                     "interaction_term",
                     "posemo",
                     "negemo",
                     "total_liwc_sentiment",
                     "liwc_polarity",             
                     "liwc_isNegative",
                     "liwc_interaction_term",
                     "liwc_isNegative_tone",
                     "liwc_interaction_term_tone")
data <- data[columns_to_keep]
save.image('~/data.RData')