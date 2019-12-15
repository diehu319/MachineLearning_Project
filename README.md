# MachineLearning_Project
A school course work for creating a machine learning prediction model.

1.	Abstract
In this project, an artificial neural network model from python package `sklearn' is used to predicting the likely performance of a student on the final exam grade based on a data set from UCI Machine Learning Repository that the data consisted approach student achievement in secondary education of two Portuguese school for Portuguese language class and the data set contains attributes, for example, include information of the 395 students' grades, demographic and social that collected by school reports and questionnaires.


2.	Introduction
Students' academic performance may likely to be influenced by various factors, such factors were considered as attributes in the dataset and input for the prediction model. The prediction model could be used by advisors to predict the students' performances based on the student's information more precise and efficient that save times from reading transcripts and basic information of the student and compare with the other students' information that the advisor knows.


3.	Overall Process
I created a predication model is to predict the Final Grade (G3) that is 0 out of 20 points. The model is created by using mlp from sklearn package from python library.


4.	Result
The model that contains 32 variables as input, the accuracy of the prediction is 46%. The second model that contains 2 variables (G1 and G2) as input, the accuracy of the prediction is 53% with some changes in the "hiddenlayersizes" parameter from sklearn: neuralnetwork:MLPClassifier().


Reference:

Database(Source data): P. Cortez and A. Silva. Using Data Mining to Predict Secondary School Student Performance. In A. Brito and J. Teixeira Eds., Proceedings of 5th FUture BUsiness TEChnology Conference (FUBUTEC 2008) pp. 5-12, Porto, Portugal, April, 2008, EUROSIS, ISBN 978-9077381-39-7. https://archive.ics.uci.edu/ml/datasets/student+performance 

Wikipedia contributors. (2019, December 5). Machine learning. In Wikipedia, The Free Encyclopedia. Retrieved 05:23, December 6, 2019, from https://en.wikipedia.org/w/index.php?title=Machinelearningoldid=929436005  

sklearn.neuralnetwork:MLPClassifier{:(n:d:):Retrievedfromhttps : ==scikitlearn:org=stable=modules=generated=sklearn:neuralnetwork:MLPClassifier:html

Robinson, S. (2018, February 6). Introduction to Neural Network with Scikit-Learn. Retrieved from https://stackabuse.com/introduction-to-neural-networks-with-scikit-learn/ 
