Model Building (model.ipynb) : Hi guys,this is a project about Forest Fire Prediction as name says, here i have taken a dataset of Forest Fire 
Occurences in india and done EDA on that and built a model using decision_tree_classifier, before that i have done cross_val_score 
to understand the model score in every regressor and classifier after all that i found decision_tree_classifier is working well with 
99.56% ,so finally i confirmed decision_tree_classifier for this model. After that i dumped the model into pickel file.

Flask Server (app.py) : After building the model i have created a flask server to the model by importing the model using pickel

HTML webpage : Here i built i webpages that is 1.forest.html & 2.after.html 
               1.forest.html : this is the home page and it takes the input from the user with three parameters (Temperature,Oxygen,Humidity)
               2.after.html: this page is for predicting the output and returns a parameter respective to the output
                  if fire occurence is there it returns "YOU ARE NOT SAFE" in red color
                  or else it returns "YOU ARE SAFE" in green color.


                  
==============================================================    over    ==========================================================================
