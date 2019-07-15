# NLP Test

This repository is a playground for assembling a speech recognition software.  
It uses the [Common Voice Database](https://voice.mozilla.org/), launched by Mozilla in 2017.

## Contents:

1. [Technical Setup](#technical-setup)
2. [Jupyter Notebook](#jupyter-notebook)
3. [Data Set](#data-set)
4. [Structure](#structure)
5. [About](#about)

## Technical Setup

Please download the data set in your corresponding language [here](https://voice.mozilla.org/en/datasets) and extract the .tar.gz archive. This might take some time; check out your disk space.  

Next, clone this repository, by downloading [here](https://github.com/anarchuser/nlp-test/) or with this command:  

`git clone https://github.com/anarchuser/nlp-test/`

Go into the git repo and install all Python 3.7 dependencies:

```
cd nlp-test/  
pip install --user -r requirements.txt
```

Go to the `interactive` (this) branch to view the Jupyter Notebooks or the `transcription-speech2text` branch for the newest development.

## Jupyter Notebook

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
