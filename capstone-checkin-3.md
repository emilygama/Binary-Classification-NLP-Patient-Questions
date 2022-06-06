## Progress Report, June 6

As of June 6 (with a deadline of June 10), I have all of my data in hand. I hand-labeled all data points including target variables for both a binomial and multinomial classification model. I have decided to go with a binary model but will at least run a basic NLP on the multinomial if I have time. I have completed a full EDA on my data, the findings of which I will include below. I have also run a basic Logistic Regression binary classification model. The result of this was good, but overfit. The score on the training data was 100%, but the score on the test data was 90%. I am now in the process of detailing a more complicated but ideally more accurate model to decrease the variance a little and get more fit scores. 

The main challenge I am facing currently is deciding which models to use or not use. I would like to try a medspacy or clinical-BERT model, but I am having issues getting them to run without the kernel dying. I intend to reach out for instructor help on this issue today (June 6). I am also starting to build out my Streamlit app. I would like to perform an example of he use-case for this model by building a chat feature within the app. I expect there to be some learning curves with this, but I have yet to encounter them.

For the rest of my time, I will be finding a better model to fit the data, potentially trying out a pre-trained clinical model to see how that would work with my data. I will also build out the Streamlit app in entirety to be prepared for presentation on Friday June 10.

As far as my EDA goes, I have found it very interesting to see what the data tells us. First, the data is slightly imbalanced, as can be seen below. I also considered doing a multinomial model, but there were too many specialties to work with. The distribution of those target classes is also below. 

![plot](../capstone/assets/class-distribution.png)

![plot](../capstone/assets/distribution-multi-nomial-class.png)

When describing the risks in my project in my previous check-in, I discussed how because of my generalization into two classes, there are questions perhaps better suited for different specialties. The issue here is that these questions are going to a generalist (internist) instead of the specific specialty. If I were to do this project with a much larger dataset, a multi-nomial classification would be my goal. However, it was not possible here. 

![plot](../capstone/assets/message-length.png)

When examining the message length, we can see that the typical messages are under or around 50 words in length, but there are still some messages that are very long. The longest message is over 370 words in length. 

Before looking at most common words, I want to provide a few random examples of questions and matched target classes from our dataset. I used a numpy random number generator to pull a row from the data. 

These first two examples are classified as 'internist'. I also included in the row the specialty if I were to do a multinomial classification model. You can see here the summarization from the original dataset as well. You can see from these two examples below that patients are asking about what lab results mean and potentially what treatments are out there for certain diagnoses. People also ask about genetic testing, symptoms of diagnoses, and types of diagnoses.
![plot](../capstone/assets/random-ex-1-pulm.png)
![plot](../capstone/assets/random-ex-3-gastro.png)

Both of these below are designated for the pharmacists. These two examples are great or showing the typical types of questions I saw when hand-labeling the data. Patients often asked about the ingredients or allergy recommendations for certain medications as well as how to take or not take medications. I also saw people ask about side effects or off-brand labels for medications.
![plot](../capstone/assets/random-ex-2-pharm.png)
![plot](../capstone/assets/random-ex-4-pharm.png)

Now, when examining the most common words below, these examples fall into line quite well. The issue I saw with the most common words is that many of the messages started with 'MESSAGE' or 'SUBJECT', which explains those top two words for each plot. However, for the overall most common words, I can see potential trends in what people are asking about. They are asking for information, help, treatment, and locations quite commonly. When we examine the binary class most common words, we can see that patient questions designated for pharmacists are asking about the name and ingredients (gluten) of the meds. Finally, for the internist class, patients are asking about information, treatments, and names. It is interesting to see many overlapping words within both of these plots. It would be interesting to pull a BERTopic analysis to see if it can identify certain topics that each patient group is asking about. I'm currently having issues running the BERTopic model without my kernel crashing. 

![plot](../capstone/assets/most-common-words.png)
![plot](../capstone/assets/most-common-words-pharmacist.png)
![plot](../capstone/assets/most-common-words-internist.png)

So far, I feel that I am in a good place to be completed and ready by Friday for my presentation. I have much work to do, but I have a clear picture in my mind of what I would like to accomplish and feel that I have a solid understanding of the data thus far. 



