# Plotting Scripts
This is a set of scripts plotting different types of data using python(3). The project is under development and may change frequently.

## Line Chart
### Plotting 1D time series. 
**Original Development Background:**
Multiple .csv files are given, each one is an individual sample recording signals from 14 equipments sharing the same x-axis (timeline). Totally, there were 24 samples coming from three large categories with each categories having 8 samples in it. 
This scripts plots all equipment signals from a single sample from top to bottom, and display all 24 samples from left to right with different colors for each category.

## Pie Chart
** This plot is highly dependent on input data, a dictionary. 
**Original Development Background:**
In our samples, we have 14 possible phases and we want to capture their transition pattern (to make a HMM). Dictionary data type was used to capture these transitions, specifically:
>Eventually, we will get a dictionary of dictionary. The upper level key is original phase, and the lower level key is the target phase. For lower level dictionary, the number in the list (this is the value of lower level dictionary) is frame counts of original phase. See example(s) below:
  5: {6: [5317, 9233], 4: [7167]}
means phase 5 can transit to phase 6 and phase 4; there are two records of transition from phase 5 to phase 6, where each time phase 5 lasts for 5137 and 9233 frames before transition, respectively. Likely, from transition from 5 to 4, the procedure lasted for 7167 frames before transition


with this type of dictionary as input, the plot shows distribution of phase transitions.


## Bar Plot
** This plot is highly dependent on input data, a dictionary, as explained above.
This plot shows all 14 phases as 14 individual bars, with each bar having colors stack on them indicating next transition. Length of stacked bar indicates how long current phase lasts before transition to the target phase.
