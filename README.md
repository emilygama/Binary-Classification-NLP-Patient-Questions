# NLP Binomial Classification for Real-Time Patient Messaging Feature
### Emily Gama, Data Scientist

[*STREAMLIT*](https://share.streamlit.io/emilygama/binary-classification-nlp-patient-questions/main/chat_app.py)

### Background
As a member of the data science team, I have been tasked with the second phase of our new online website product on medlineplus.gov from the US National Library of Medicine. This product allows consumers to input a question into our embedded chat feature. Our team has already built out a model to summarize the questions into a basic and logical form. This is where I come in: I will be building the model to differentiate between question content and direct them to our on-call specialists for answering. This chat feature will function similarly to an online customer service chat platform. In this second phase, I will focus on the classification feature and building out an initial chat interface to progress to the engineering team. 

Explicitly, my project will aim to build a binomial classification NLP model that identifies patient needs from an incoming message and matches that patient with a specialist to answer in real-time. This will be done using the MeQSum corpus, a dataset of 1,000 patient questions pulled from the US National Library of Medicine. These questions were then summarized by medical experts. The model I will build will use the natural patient question to identify whether the patient is seeking a pharmacist or internist to answer their question. I will build a chat-feature Streamlit app to highlight the importance of this model's work. This model would fit into a larger project outside the scope of this course but buildable in the long-term. The use case for a product like this would be embedded into a medical information website as a question asking chat feature. Patients would be able to ask a doctor a question, their question would be sorted to the correct specialist, and a specialist would be able to answer them.

### Data
Patients who submit questions on this website are searching for answers, regardless of who it comes from. However, because of our classification work, we can see that patients asking for internists are interested in diseases, their treatment, syndromes, the causes of syndromes, and specific named issues like strokes, hormones, hernias, etc. They are seeking knowledge about diagnoses in general. Compared to that of the pharmacist class, they are seeking out knowledge related to specific medicaitons/drugs, dosages, how the drugs are to be taken (instructions), pharmacies, and ingredients. Several forms of the word medication (medication, meds, drugs) are used to refer to their subject. Words like lower and build can refer to the mechanism of action for these drugs (how they work). 

### Concerns
The risks and issues with this project are clear from the outset. Ideally, I would have more data points than 1,000, more time to hand label questions (or use a program), and would be able to build a multi-class target (several specialties). When I initially labeled the data, I had about 20 classes of different specialties from pediatrician to infectious disease to dentists. I quickly realized that for this size of dataset, a multi-class project would not be feasible. Therefore, I trimmed it down to differentiating between pharmacist and internist (general MD or primary care physician). I made this decision because I noticed several medicaition-related questions that would best be answered by a pharmacist. This binary differentiation fell into place naturally. With this, however, I realize that the medical questions being classified to 'internist' may not always be relevant to that internist's work. Because there are a broad range of questions in this dataset, there are some questions that may be more suited for an ophthalmologist, dentist, pulmonologist, oncologist, etc. Because I made this a binary classification model, I am accepting that this project will help me identify a good starting point for what could be a great model in production. Further, because I hand-labeled the data, there is a risk that I mislabeled or misunderstood the question. To minimize this risk, I ensured I did research on symptoms, conditions, medications, and concerns when I did not have extensive background knowledge on the topic. I believe I labeled the questions as accurately as I could and to the best of my knowledge. 

### Modeling
The best performing model is a default Random Forest Classifier. Through the modeling process, I realized that using the raw question data was hurting model performance. This seems to be due to the inpredictability of the patient questions. I decided that using the summarized questions instead would be better for modeling. While I don't have access to that model or code as I am working just within this second phase, I have access to the summarized question output. When I considered this issue further, I realized that it makes sense in production for raw data to be filtered through a summarizer before working through the classifier model. The summarizer here acts almost like a preprocesser for the data, and after redoing my model with the summarized data, it performed with much more accuracy. I particularly think Random Forest works so well because it uses the randomization and de-correlating to reduce the high variance issues we saw with other models like Logistic Regression. Because of this, the model became ready for production in a chat-based app. 

When considering real-time use of this product, I am concerned that patients who need immediate treatment but may not know might ask questions seeking help or explanation. I think it would be important to include a disclaimer in or near the chat feature that tells the patient symptoms that need emergent attention and to call 911 instead of using the chat feature. This product should be for explanation and knowledge assistance. Any patient seeking immediate medical care needs to know that they will not find it here. 

### Conclusion
At this point, it would be beneficial for this model to be applied to a larger data set with more specialties to produce a better functionality on large scale. This model as we can see works well for our binary classification, but the next step is to test it in a more broad sense.


### Sources: 
* [*Access Data*](https://paperswithcode.com/dataset/meqsum)
* [*Streamlit Help Pt 1*](https://github.com/andfanilo/social-media-tutorials/blob/master/20220124-streamlitchat/streamlit_app.py)
* [*Streamlit Help Pt 2*](https://github.com/AI-Yash/st-chat/blob/main/streamlit_chat/__init__.py)
* [*Medical Disclaimer Pt 1*](https://www.massgeneral.org/notices/disclaimer)
* [*Medical Disclaimer Pt 2*](https://www.insted.us/emergency-disclaimer)




