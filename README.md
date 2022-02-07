# Forecast-Challenge-1-Code-ECON-8710
My professor issued a challenge to see who take a data set and use it to predict the next year most accurately. My entry predicted the data most closely by MSE, winning the competition. This is the Python code I used to help come up with my answer.

The repository contains the data set issued by my professor, the python code I used, a writeup of my method, and plots of my results.

The data set contains months and sales for each months. The goal was to predict the next year's sales.

My python code reorganizes the data into a plottable format, which I used to analyze the data. I then created binary variables for certain months to use in a regression. I saved the formatted data and dummy variables in a new csv which I then performed regressions on in R.

To understand my full process, please refer to the pdf of my writeup. I have also attached plots of the original data set as well as my prediction. The original data set is titled "Graphfig.png" and my prediction is titled "forechal1pred.png" and the predicted sales values are circled in red.
