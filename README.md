# A/B Testing
## Introduction 
A/B testing (also known as bucket testing or split-run testing) is a user experience research methodology. A/B tests consist of a randomized experiment with two variants, A and B. It includes application of statistical hypothesis testing or "two-sample hypothesis testing" as used in the field of statistics. A/B testing is a way to compare two versions of a single variable, typically by testing a subject's response to variant A against variant B, and determining which of the two variants is more effective.

## Classical A/B Testing

The main goal of the test is to disprove the null hypothesis. Null hypothesis means our control and test group don’t have difference, or the change we introduced don’t have visible or valuable impact. And if we see any change they are from randomness or luck. Alternate Hypothesis is the opposite of null hypothesis. 


## Sequential A/B Testing
The best part about sequential A/B testing is that it gives users a chance to finish experiments earlier without increasing the possibility of false results.  Sequential A/B testing in its turn allows multiple checks on every step ensuring that error level won’t exceed 5%. 

## A/B testing using Machine Learning

An attractive benefit to Machine Learning is that we can combine multiple approaches to gain insights. In the machine learning setting, we can also get valuable info on the contribution of every feature to getting a higher conversion rate.

To begin machine learning A/B testing we need a dataset. It’s critical to have an equal number of elements in the control and exposed groups. The machine learning models that we used were **Logistic Regression**, **Decision Tree** and **XGBoost**.

## Code

Our classical and sequential A/B testing code can be found in the **sequential_testing.ipynb** jupyter notebook in the **notebooks** folder. 
Our ML based A/B testing code can be found in the **Task2.ipynb** jupyter notebook in the **notebooks** folder.
To install the necessary dependencies, execute the command 
```$ pip install -r requirements.txt"```

