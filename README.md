# Emotions and Information Diffusion on Social Media: A Replication in the Context of Political Communication on Twitter

This repository contains code and data used in the research paper

> Emotions and Information Diffusion on Social Media: A Replication in the Context of Political Communication on Twitter. Hagemann, L., Abramova, O.

which has been accepted for publication in [AIS Transactions on Replication Research](https://aisel.aisnet.org/trr/).

## Process Documentation

The following paragraphs should give you a good overview of how to use the scripts in this repository given previous exposure to the command line, python and R. Please see the corresponding publication for further details.

Following the steps outlined below should allow you to replicate our findings, beginning with the collection of tweets. Please be aware that the availability of tweets might have changed since we collected the original data set. For entry-point ready data-sets, please take a look at the "Data" section below.

Please note, that this code makes some assumptions about naming schemes, directory structures, ... that might be not documented. Therefore, changes to the code will be necessary in order to run it successfully. We sincerely hope that this does not affect things other than paths and filenames.

Please reach out with any questions directly or open a ticket in this repository.

## Data Collection

For the collection of our data set we used the [Twitter API in V2](https://developer.twitter.com/en/docs/twitter-api) and its official [python3 package](https://github.com/twitterdev/search-tweets-python). The `yaml` file used for the configuration of the python program can be found in the `collection` folder. Execution should look similar to this:

```
python3 search_tweets.py --credential-file ../../.credentials.yaml --config-file ../../api_config.yaml --no-print-stream --output-format a
```

## Data Preprocessing

Run `transform_json.py` on the `JSON` output of the twitter API to transform it into CSV for further processing. The script takes to arguments on the command line, where the first one is the name of the JSON file to be processed and the second one is the desired name of the output.
Afterwards, `scrape_retweets.py` can be used to collect all retweets of the scraped tweets, even ones that were not retrieved by the original API query. You will need to set the correct path to the Twitter API script you installed above and you will need to have [`Sultan`](https://pypi.org/project/sultan/) installed. The collected retweets should also be preprocessed following the steps outlined previously.
The necessary code can be found in the `preprocessing` folder.

## Sentiment Analysis

After preprocessing all tweets, use the `add_sentiment_data.R` script in the `preprocessing` folder as a pointer on how to add the SentiStrength output to the collected data set. You will need to have [`SentiStrength`](http://sentistrength.wlv.ac.uk/) and the German Language Pack downloaded. The call will probably look something like this:

```
java -jar SentiStrengthCom.jar input ../tweet_text.csv sentidata ~/abc/SentiStrength/SentiStrength_Data/ EmotionLookupTable ~/abc/SentiStrength/SentiStrength_Data/EmotionLookupTable_v5_fullforms.txt explain
```

With the same technique, analyze the collected tweets using [LIWC](https://www.liwc.app/) and again add the output to the main `CSV` file holding your data.

## Data Analysis

Inside the `data` directory, an `R` script for the final preparation step of the data (`data_prep`) can be found. Alongside, you will also find the scripts that we used to create the publication-ready data-set as well as the published list of tweet IDs.

You can use these IDs to scrape our [exact data collection yourself](https://github.com/DocNow/hydrator), or use the provided data-set to execute our modelling code provided in `analysis.rmd`. We also provide a knitted HTML version of our modelling notebook, with the results created on our machine.

For some summary statistics regarding active tweet authors, you will need to have your own tweet-collection, since we cannot provide the data-set including author-names. The relevant scripts can be found inside of the `analysis` directory.

## Technical Notes

This code was developed for and used on a UNIX system. If you are on windows, intricacies like line-breaks might need further adjustments in the code.
Please note, that this code makes some assumptions about naming schemes, directory structures, ... that might be not documented. Therefore, changes to the code will be necessary in order to run it successfully. We sincerely hope that this does not affect things other than paths and filenames.

## License

Copyright © 2022 Linus Hagemann, Olga Abramova.

All code is published under the MIT license.

Our data-sets are made available under CC BY-NC-SA 4.0.
