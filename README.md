# NLP Binomial Classification for Real-Time Patient Messaging Feature
### Emily Gama, Data Scientist

Problem Statement: This project will aim to build a binomial classification NLP model that identifies patient needs from an incoming message and matches that patient with a specialist to answer in real-time. This will be done using the MeQSum corpus, a dataset of 1,000 patient questions pulled from the US National Library of Medicine. These questions were then summarized by medical experts. The model I will build will use the natural patient question to identify whether the patient is seeking a pharmacist or internist to answer their question. I will build a chat-feature streamlit app to highlight the importance of this model's work. This model would fit into a larger project outside the scope of this course but buildable in the long-term. The use case for a product like this would be embedded into a medical information website as a question asking chat feature. Patients would be able to ask a doctor a question, their question would be sorted to the correct specialist, and a specialist would be able to answer them.

Metrics: The most important metrics here will be accuracy and the F1 score. Msot importantly, I want to ensure I prioritize accuracy. In the medical field, it is of utmost importance that what we are telling our patients is accurate (predicting correctly overall) for their safety. However, it is also important to ensure that my model is not disproportionately favoring one class over another. This is why I will also look at the F1 score. The F1 score provides the harmonic mean between precision and recall (sensitivity). Now, I am truly after recall as it tells us about the correct positive predictions of the model, but because I have imbalanced data, using the F1 score will help evaluate the model's fairness in classification as well. This is important in identifying better or worse models for my use-case. 

Risks and Assumptions: For this project, I am attempting the minimum valuable project for this use case. Ideally, I would have more data points, more time to hand label questions (or use a program), and would be able to build a multi-class target. When I initially labeled the data, I had about 20 classes of different specialties from pediatrician to infectious disease to dentists. I quickly realized that for this size of dataset, a multi-class project would not be feasible. Therefore, I trimmed it down to differentiating between pharmacist and internist (general MD or primary care physician). I made this decision because I noticed several medicaition-related questions that would best be answered by a pharmacist. This binary differentiation fell into place naturally. With this, however, I realize that the medical questions being classified to 'internist' may not always be relevant to that internist's work. Because there are a broad range of questions in this dataset, there are some questions that may be more suited for an ophthalmologist, dentist, pulmonologist, oncologist, etc. Because I made this a binary classification model, I am accepting that this project will help me identify a good starting point for what could be a great model in production. 

[*Access Data*](https://paperswithcode.com/dataset/meqsum)

