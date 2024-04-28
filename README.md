# NCAA_Bracket_Prediction
This dashboard displays NCAA predictions for each team's likelihood of making/ending on a certain bracket.

Deployment URL: https://ncaa-bracket-prediction.onrender.com/

# Documentation
## Overview:
- This dashboard enables the user to view the probabilities of a team making a specific bracket based off of a prediction made from a predictive model. The design was made to enable intuitive controls, such as simply pressing on dropdowns, to display desirable data for those looking forward to seeing predictions being made.
## Instructions:
- There are two dropdowns at the top of the dashboard right below the main header. They are both used to select teams, and by selecting a team from each of them, you will see their probabilities being plotted in a bar graph and pie chart below.
- When selecting two teams, the bar graph will combine the two probabilities to allow the user to directly compare the data, and two separate pie charts will be displayed to showcase the probabilities in a different manner, one for each team.
## Process:
- The following text will detail the process behind developing this dashboard, with the first step involving the reading of the data, followed by the steps being elaborated upon below.
### Cleaning:
- Columns in the dataset that contained too much not available (NA) data were dropped to prevent too much data from being lost in the analysis.
- The data would be separated into X and Y:
  - X contains the features, excluding the Team and Competition Name since they were both the target variables.
  - Y contains the target variable, which is the Competition Name. This decision was made since the model is predicting the likelihood of a team winning rather than predicting the individual performance of a team.
- With the X and Y set up for training, we can proceed to develop the model.
## Model Development:
- The model used here was a Decision Tree Classifier (DTC), which made it easier to deal with both numerical and non-numerical data.
- The train/test distribution for the model was 80/20, and so the X and Y data would be split into X_train, X_test, Y_train, and Y_test in that regard.
- The model would then fit with the X_train/Y_train data and test the validation accuracy with the X_test/Y_test data.
## Export Prediction:
- After getting the predictions for each team reaching a certain bracket, a data dictionary would be created, representing each team's probability in reaching a certain bracket in March Madness. The exported json file can be found under the data folder.
## Regarding Dataset:
- The dataset used in the data_cleaning.ipynb file CANNOT be shared outside, so permission from the owner of that dataset is needed to run the code and predictive model training.
