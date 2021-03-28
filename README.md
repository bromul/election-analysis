# PyPoll with Python

## Overview of Election Audit
This project analyzed voter data to certify the results of a U.S. congressional election in a Colorado precinct.

### Purpose
We had been asked by Tom, a Board of Elections official, and his manager Seth, to create a code that could quickly count through the voter data in a U.S. congressional election over the Colorado counties of Jefferson, Denver, and Arapahoe, in order to certify the results for the election commission. To do this, we were asked to verify the total number of votes cast, how many votes each candidate received (in both gross and precentage terms), and determine the winner of the election. Once we finished with that, we updated our code to verifiy the gross and percentage amount of votes received in each of the three counties.

## Election-Audit Results

### Results

Through our analysis, we determined:

- Total Votes: 367,711
- Votes by County:
  - Jefferson:  10.5%    (38,855)
  - Denver:     82.8%   (306,055) 
  - Arapahoe:    6.7%    (24,801)    
- County with Largest Turnout: Denver
- Votes by Candidate:  
  - Charles Casper Stockham:  23.0%    (85,213)
  - Diana DeGette:            73.8%   (272,892)
  - Raymon Anthony Doane:      3.1%    (11,606)
- Election Winner: Diana DeGette
  - Vote Count: 272,892
  - Percentage: 73.8%


You can see the code's output below:

![Analysis of Congressional Election](https://github.com/bromul/election-analysis/blob/main/Images/election_results.PNG)

  
## Election-Audit Summary
As seen above, this script was written for, and can quickly verify, this Colorado congressional election. However, it can be reapplied to any election that may need to be counted or verified in the future, with only a few simple modifications. Though not an exhaustive list of modifications that could be made, hopefully this will provide you with an understanding of how this code can be generalized for many different elections.

Firstly, depending on he name of election file you want to import, and the path to it on your local machine, you will have to change the path and name in *file_to_load*. This will also be true if you want to record the election analysis in a different folder or under a different name, in which case you will need to edit *file_to_save*. 

![Variables to Load and Save from a Path](https://github.com/bromul/election-analysis/blob/main/Images/code_file_to_load_save.PNG)

Modifying these lines of code will be essential to ensuring you are able to import the proper files.

Additionally, before running the code on a different CSV, it's important to determine which colunms correspond to which data - and to edit the appropriate lines. For example, in this election dataset, the county's name was provided in column 2 and the candidate's name was provided in column 3. This meant that when we assigned the variables *candidate_name* and *county_name*, we hardcoded them as *row\[2]* and *row\[1]* respectively. 

![Candidate and County Names Set to Their Columns](https://github.com/bromul/election-analysis/blob/main/Images/candidate_county_name_col.PNG)

When editing these lines for the appropriate columns, you have the options of (a) hardcoding them again, or (b) creating variables at the top of the code that correspond to the columns the data may be in, as demonstrated below. This allows the code to be more generalized and more easily adapted across multiple different elections.

![Setting Variables to the Columns with Candidate and County Names](https://github.com/bromul/election-analysis/blob/main/Images/candidate_county_var_col.PNG)

Finally, you may want to change the names of many of the varibles and output, depending on the specifics of the election that's being verified. Variables such as *county_vote* or output that says "Largest County Turnout" don't make much sense when you're looking at boroughs or states instead of counties. Though the code will still run the same way without the variable names being changed, it can greatly improve quality of life and the facility of data presentation.


  
