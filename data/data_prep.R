# PLEASE NOTE:
# When executing this script, it is assumed that your data collection is already loaded into an R session
# under the name `data`.
library(here)

# otherwise log transformation fails
data <- data[data$author_follower_count > 0,]

# cleaning up some data types
data$negemo <- gsub(",",".", data$negemo)
data$posemo <- gsub(",", ".", data$posemo)
data$negemo <- as.numeric(data$negemo)
data$posemo <- as.numeric(data$posemo)
data$author_verified <- ifelse(data$author_verified == "True", TRUE, FALSE)
data$is_Negative <- as.numeric(data$is_Negative)
data$author_verified <- as.numeric(data$author_verified)

# new features based on Stieglitz2013
data$total_liwc_sentiment <- data$negemo + data$posemo

data$liwc_polarity <- data$posemo - data$negemo
data$liwc_isNegative <- ifelse(data$liwc_polarity < 0, 1, 0)
data$liwc_interaction_term <- data$liwc_isNegative * data$total_liwc_sentiment

save(data, file = here('prod.RData'))
