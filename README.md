# NLP Test

This repository is a playground for assembling a speech recognition software.  
It uses the [Common Voice Database](https://voice.mozilla.org/), launched by Mozilla in 2017.

## Contents:

1. [Technical Setup](#technical-setup)
2. 
3. 
4. [Structure](#structure)
5. [About](#about)

## Technical Setup

## jupyter Notebook

## Data Set

The Mozilla Voice database consists of one data set for each of over 20 different languages.  
Each data set consists of a certain amount of audio clips - one specific sentence spoken in the respective language - and information about the clips.  

The information is stored in TSV files, each file containing one table where the values are separated by tabulators and newlines.  
They look like this:  

| client_id | path | sentence | up_votes | down_votes | age | gender | accent |
|-----------|------|----------|----------|------------|-----|--------|--------|
| ...       | ...  | ...      | ...      | ...        | ... | ...    | ...    |

"client_id" is individual for every speaker, and "path" refers to the name of the clip.  
Up and Down votes indicate how well a sentence is spoken; a clip needs two upvotes to be counted as "validated".  
The last three columns are demographic data; they are not necessarily available.

## Structure

## About
