Scientific Explanation
======================

This repository holds all the code built for 

which is presented in the following publications:
* lien 1
* lien 2

Detailed steps to reproduce the specific results presented in each of these paper are included. 
The results presented in these publications were produced from a common set of tools and data.

However, the subject being incredibly rich, both in terms of data and of philosophical inquiry, many questions remain unexplored.
The whole toolset is thus made available to anyone interested in pursuing further investigations.

We organised the repository to ensure both the reproducibility of the results presented in each publications, and the availability of the toolset to pursue further investigations.

The general instructions and specifications can be found below, and the details specific to each of the publications are located their respective directories.


lien vers le data

Project Structure
-----------------

We organised the repository to ensure both the reproducibility of the results presented in each publications, and the availability of the toolset to pursue further investigations.

Each article has its own subdirectory holding the code and instructions needed to reproduce the results.

Core code used across the project is stored in the `/lib` directory. 
The DocModel class is used as a base data structure representing the different documents forming the corpus. 
A DocModel objects is created for each of the XML files made available by BioMed, holding all the relevant data extracted from the raw XML.
Storing the DocModels as pickles allows to easily store the data for later use.
A working corpus can be formed by filtering the DocModels to only keep those meeting certain criterion, like minimal text length or specific metadata values.

From then on, the basic workflow consists of using a generator to cycle through the docmodels, each time reading some data or performing some operation.
While this process is somewhat slow, it helps keep the memory footprint to a minimum by storing only the relevant data.
Some useful generator functions can be found in `lib/utils/generators.py`

The code used in the various analyses of textual content is located in `lib/models`. 
Each type of analysis is represented by a class (acting as a type of model) holding all the relevant logic, which can be updated with the data from a DocModel generator.
Starting an analysis as simple as creating an instance of the class, using the init method to set parameters.
In most cases, these classes have an update method which should be called once for each DocModel, passing the relevant data. 
Once done updating the model, the data can usually be exported as a DataFrame using the as_df method.
Note that the model itself can be stored as a pickle file, which is usually recommended.
In certain cases, converting the results to a DataFrame can require a lot of memory and lead to errors.
However, the models themselves are usually relatively lightweight, so saving them before exporting to a dataframe is a good precaution to avoid having to repeat the updating process, which can take a fair amount of time.
Finally, these analysis tools were designed to be flexible (most of the update methods work from a generic data type, like a list of strings or a list of Tag-like objects) 
and could easily be used with a different corpus.



Article 1
---------

Diagram

(shenanigans in step 1, will be small differences in the working corpus and docterm matrix if you run from scratch)
(can use legacy setting to reproduce)

Article 2
---------


Lib
---


Viz
---

ref to template


