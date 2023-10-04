## Web APIs & NLP

### Problem Statement

In this study, we aim to delve into the online communities of two popular subreddits, r/Marvel and r/DCcomics, to understand the unique characteristics, discussions, and trends within each subreddit outside of superhero names

Our analysis will encompass various aspects, including word count, sentiment analysis using natural language processing (NLP), frequently used keywords, and discussions around prominent superheroes from each universe. By applying these methodologies, we seek to uncover patterns, preferences, and differences in content between these two subreddits. 

### Methodology:

* 		Data Collection: Utilizing Reddit's API, data will be gathered on the number of subscribers, posts, and other relevant metrics for both subreddits over a selected time period.
* 		Text Analysis: Natural Language Processing (NLP) techniques will be applied to analyze the sentiment of posts and comments, extract keywords, and classify content types. This will help us understand the types of discussions happening in these forums
* 		Models: Running multiple models and predictions, removing popular Bi-Gram and Superhero names to understand if these factors play a role in accuracy.
* 		Data Visualization: To facilitate easy comparison and interpretation, data will be visualized using charts, graphs, and heatmaps.
* 		Hypothesis Testing: Statistical analysis may be employed to test hypotheses regarding user engagement differences between the two subreddits.
* 		Content Analysis: A manual review of a subset of posts and comments will be performed to validate the results from the automated NLP analysis.


### Conclusions

In conclusion, a consistent observation arising from the analysis of posts across both subreddits is the prevalence of discussions surrounding Marvel superheroes in comparison to DC superheroes. Furthermore, Marvel's iconic characters hold greater recognition than DC's except for Superman and Batman. The model's ability to maintain a high level of predictive accuracy even after eliminating dominant bi-grams and superhero names reflects its robustness in capturing meaningful patterns beyond surface-level linguistic features.

Both subreddits exhibited slightly positive sentiment, with the DC subreddit showing a slightly higher average sentiment polarity compared to the Marvel subreddit. However, it's important to account for Marvel's greater engagement levels, which may influence sentiment scores. This investigation underscores the intricate dynamics of these online communities and provides valuable insights into user preferences, linguistic nuances, and sentiment tendencies within the context of the Marvel and DC universes. 


### Description

In week four we've learned about a few different classifiers. In week five we'll learn about webscraping, APIs, and Natural Language Processing (NLP). This project will put those skills to the test.

For project 3, your goal is two-fold:
1. Using Reddit's API, you'll collect posts from two subreddits of your choosing.
2. You'll then use various NLP techniques to process your data before training a range of classifiers to determine where a given post came from.


#### About the API

In 2023, Reddit proposed and underwent a series of changes to its API that greatly affected the ways that users, developers, and academics interact with and access the troves of data that its community freely creates.

While the cost of data storage cannot be ignored, the monetization of its API has led to a shutdown of massively popular third-party and stifled [important research](https://arxiv.org/search/?query=reddit&searchtype=all&source=header) in the social sciences (community formation/network analysis, hate speech, discourse analysis, etc.), cybersecurity (bot detection), and—importantly for us this week—the very large and diverse world of natural language processing (semantic analysis, translation, topic modeling, disambiguation, relationship extraction, etc).

While APIs like Pushshift that collected and stored Reddit's data from its inception are no longer accessible, we can still retrieve a limited amount of data directly from [Reddit's API](https://www.reddit.com/dev/api/). As with anytime you begin interacting with a new tool, you should familiarize yourself as much as possible with the documentation.

**We will do a walkthrough of how to access and submit a simple request to the Reddit API together.**

---
## Checkpoints and Advice

If you aren't familiar with [reddit](https://www.reddit.com/), go check it out and browse different subreddits. Each subreddit is like a forum on a different topic. [Here's a list of subreddits by topic.](https://www.reddit.com/r/ListOfSubreddits/wiki/listofsubreddits)

Data Choices
- In your project you can classify posts, comments, titles, or some combination of those things. What you choose will partly determine how difficult your data cleaning will be and how challenging the classification task will be for your algorithms. In your presentation and executive summary, **tell us what you used**.
- You can also include other information from posts or comments as features, but you must include some text.

Subreddit Selection
- The more similar the subreddits are, the more challenging (and interesting?!) your project will become.
- **By the EOD Thursday, 7/27/2023, you must input your chosen subreddits into [this spreadsheet](https://docs.google.com/spreadsheets/d/17lggTAo37jWLajxamAukqvh506rqsxOxpXXsKnbHv9I/edit?usp=sharing). You may not choose the same two subreddits as one of your peers: first come, first served.** Please include a breakdown of the post count for each as well.

Data collection
- You should have a script written to retrieve data from your subreddits of choice by the EOD Thursday, 7/27/2023. Because the API only allows us to retrieve 1000 of the most recent new and popular posts at time, this script should be written so that you can execute it from the command line at regular intervals.
- The more data you can pull the better for your classifier. **You will want data from at least 3000 unique, non-null posts from each subreddit.**
- We will provide supplementary data once you've retrieved a sufficient amount on your own.
- Requirements for this script will be given below.

---

### Requirements

- Gather and prepare your data using the `requests` library in a Python script.
- Script requirements:
    - First time it runs:
        - Gets user input on subreddits they want to collect information from
        - Asks user for their API credentials
        - Stores this information in a JSON file
    - Submits requests to API until maximum number of posts have been retrieved
    - Writes/appends post data to a singular file
    - Creates and updates a transaction log recording the number of posts retrieved per script execution, the datetime of its execution, and the total number of posts retrieved to date
        - We will be examining this file to ensure that the script was executed over several days' time
    - Other considerations
        - Added functionality to drop data you are confident you will not want for EDA or modeling
        - Added functionality to drop duplicate posts from each successful round of API requests
        - *Advanced bonus*: schedule a process for the script to be run automatically at regular intervals to avoid having to do it manually
- **Create and compare at least two models**. These can be any classifier of your choosing: logistic regression, Naive Bayes, KNN, Random Forest Classifier, etc.
  - **Bonus**: use a Naive Bayes classifier
- You **must build a robust commit history** on GHE for this project, with the first commit no later than next Monday, 7/31/23.
- A Jupyter Notebook with your analysis for a **peer audience of data scientists.**
- An executive summary of your results.
- A short presentation outlining your process and findings for a semi-technical audience.

**Pro Tip:** You can find a good example executive summary [here](https://www.proposify.biz/blog/executive-summary).

---

### Necessary Deliverables / Submission

- Code and executive summary must be in a clearly commented Jupyter Notebook.
- You must submit your slide deck.
- Deadlines:
    - **[Subreddits approved](https://docs.google.com/spreadsheets/d/17lggTAo37jWLajxamAukqvh506rqsxOxpXXsKnbHv9I/edit?usp=sharing)**: 5 PM PST, Thursday, 7/27/31
    - **Script: 9 PM PST**, Thursday, 7/27/31
    - **First execution**: EOD, Thursday, 7/27/31
    - **First commit of many**: 5 PM PST, Monday, 7/31/31
    - **Materials submitted**: 9 AM PST, Friday, 8/11/31
    - **Presentation**: 930 AM PST, Friday, 8/11/31

---

## Rubric
You should make sure that you consider and/or follow most if not all of the considerations/recommendations outlined below **while** working through your project.

For Project 3 the evaluation categories are as follows:<br>
**The Data Science Process**
- Problem Statement
- Data Collection
- Data Cleaning & EDA
- Preprocessing & Modeling
- Evaluation and Conceptual Understanding
- Conclusion and Recommendations

**Organization and Professionalism**
- Organization
- Visualizations
- Python Syntax and Control Flow
- Presentation

**Scores will be out of 30 points based on the 10 categories in the rubric.** <br>
*3 points per section*<br>

| Score | Interpretation |
| --- | --- |
| **0** | *Project fails to meet the minimum requirements for this item.* |
| **1** | *Project meets the minimum requirements for this item, but falls significantly short of portfolio-ready expectations.* |
| **2** | *Project exceeds the minimum requirements for this item, but falls short of portfolio-ready expectations.* |
| **3** | *Project meets or exceeds portfolio-ready expectations; demonstrates a thorough understanding of every outlined consideration.* |


### The Data Science Process

**Problem Statement**
- Is it clear what the goal of the project is?
- What type of model will be developed?
- How will success be evaluated?
- Is the scope of the project appropriate?
- Is it clear who cares about this or why this is important to investigate?
- Does the student consider the audience and the primary and secondary stakeholders?

**Data Collection**
- Was enough data gathered to generate a significant result?
- Was data collected that was useful and relevant to the project?
- Was data collection and storage optimized through custom functions, pipelines, and/or automation?
- Was thought given to the server receiving the requests such as considering number of requests per second?

**Data Cleaning and EDA**
- Are missing values imputed/handled appropriately?
- Are distributions examined and described?
- Are outliers identified and addressed?
- Are appropriate summary statistics provided?
- Are steps taken during data cleaning and EDA framed appropriately?
- Does the student address whether or not they are likely to be able to answer their problem statement with the provided data given what they've discovered during EDA?

**Preprocessing and Modeling**
- Is text data successfully converted to a matrix representation?
- Are methods such as stop words, stemming, and lemmatization explored?
- Does the student properly split and/or sample the data for validation/training purposes?
- Does the student test and evaluate a variety of models to identify a production algorithm (**AT MINIMUM:** two classification models, **BONUS:** try a Naive Bayes)?
- Does the student defend their choice of production model relevant to the data at hand and the problem?
- Does the student explain how the model works and evaluate its performance successes/downfalls?

**Evaluation and Conceptual Understanding**
- Does the student accurately identify and explain the baseline score?
- Does the student select and use metrics relevant to the problem objective?
- Does the student interpret the results of their model for purposes of inference?
- Is domain knowledge demonstrated when interpreting results?
- Does the student provide appropriate interpretation with regards to descriptive and inferential statistics?

**Conclusion and Recommendations**
- Does the student provide appropriate context to connect individual steps back to the overall project?
- Is it clear how the final recommendations were reached?
- Are the conclusions/recommendations clearly stated?
- Does the conclusion answer the original problem statement?
- Does the student address how findings of this research can be applied for the benefit of stakeholders?
- Are future steps to move the project forward identified?


### Organization and Professionalism

**Project Organization**
- Are modules imported correctly (using appropriate aliases)?
- Are data imported/saved using relative paths?
- Does the README provide a good executive summary of the project?
- Is markdown formatting used appropriately to structure notebooks?
- Are there an appropriate amount of comments to support the code?
- Are files & directories organized correctly?
- Are there unnecessary files included?
- Do files and directories have well-structured, appropriate, consistent names?
- Is there a robust commit history?

**Visualizations**
- Are sufficient visualizations provided?
- Do plots accurately demonstrate valid relationships?
- Are plots labeled properly?
- Are plots interpreted appropriately?
- Are plots formatted and scaled appropriately for inclusion in a notebook-based technical report?

**Python Syntax and Control Flow**
- Is care taken to write human readable code?
- Is the code syntactically correct (no runtime errors)?
- Does the code generate desired results (logically correct)?
- Does the code follows general best practices and style guidelines?
- Are Pandas functions used appropriately?
- Are `sklearn` and `NLTK` methods used appropriately?

**Presentation**
- Is the problem statement clearly presented?
- Does a strong narrative run through the presentation building toward a final conclusion?
- Are the conclusions/recommendations clearly stated?
- Is the level of technicality appropriate for the intended audience?
- Is the student substantially over or under time?
- Does the student appropriately pace their presentation?
- Does the student deliver their message with clarity and volume?
- Are appropriate visualizations generated for the intended audience?
- Are visualizations necessary and useful for supporting conclusions/explaining findings?


---

### Why did we choose this project for you?
This project covers three of the biggest concepts we cover in the class: Classification Modeling, Natural Language Processing and Data Wrangling/Acquisition.

Part 1 of the project focuses on **Data wrangling/gathering/acquisition**. This is a very important skill as not all the data you will need will be in clean CSVs or a single table in SQL.  There is a good chance that wherever you land you will have to gather some data from some unstructured/semi-structured sources; when possible, requesting information from an API, but often scraping it because they don't have an API (or it's terribly documented).

Part 2 of the project focuses on **Natural Language Processing** and converting standard text data (like Titles and Comments) into a format that allows us to analyze it and use it in modeling.

Part 3 of the project focuses on **Classification Modeling**.  Given that project 2 was a regression focused problem, we needed to give you a classification focused problem to practice the various models, means of assessment and preprocessing associated with classification.   
