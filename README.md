# Project2-Team-Oak

## Project Description

Users will be able to access various statistics about the data set.
- Mean and median, max and min, standard deviation, and range for the dollar price of the Big Mac on a yearly basis.
- PPP via Big Mac price. We are interested in the purchasing power of the dollar in other countries. Suppose that P1 and P2 are the prices of a big max measured in USD (relative to the given exchange rate) in the United States and a second country, respectively. You can compute the PPP for the Big Mac by the quotient PPP = P1 / P2. 
    - If PPP > 1, then the goods are cheaper in the second country, and their currency is undervalued (retire there).
    - If PPP < 1, then goods are more expensive in the second country, and their current is overvalued (don't retire there).
- PPP for each region. We can create a heat map that identifies which countries have a stronger currency (in terms of the Big Mac Index). 
- Analyze the change in the PPP over time for a specified countries. 


## Requirements

### "The Data"
Select an external data source. It must:
- Be open in nature (no paid data sources)
- Be available in CSV (comma separated value) or JSON (javascript object notation)
- Contain at least 200 individual entries

### "The Application"
Write a python application to provide an interface and analysis of the data source.

### Technical Requirements:
- The application must be written in Python
- Provide an interactive terminal interface
- Handle any exceptions or errors gracefully
- Let the user continue running the application until they choose to exit the program
- Allow the user to choose which file/source to read data from
- Provide an option to the user to examine individual entries
- Provide an option to the user to examine sets of similar data based on a sort and/or filter functionality

## Style Guide
- Classes: PascalCase
- Functions and Methods: camelCase
- variables: snake_case
