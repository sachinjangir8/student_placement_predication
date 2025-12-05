first create the envirement using--
        python -m venv envname
        py -3.10 -m venv env310
activate it using--
        envname\scripts\activate
create readme.md--
setup the github--
created the .gitignore from github and pull it to the project--
createfiles--
        setup.py
            with setup.py i am enable to setup my ml project as a package then anybody can use it to build it
        requirements.txt
create src folder--
        entire project will be in src
     ---------------------------   
connect requirements.txt with setup.py using (-e .)-it will trigger setup .py when req.txt will be run but it will give a problem --like when we will install our req.txt it will add -e. in getreq[] function of our setup.py so make a condition to remove it
     ----------------
now run pip install -r requirements.txt
        when u run it,it will create the --student_placement_predication.egg-info  ------------------------------------------------------------------------------
        till now to create an ml project you have to do this
-------------------------------------------------------------------------------------------------------------



now starting the project---
__init__.py is used to use the folder as package which can be exported and imported in some other file location
src--
components folder---
        (data injection.py --reading the file from db or some other file location,spliting data in train test)
        (data transformation --here data from categrical feature to numeric feture ,one-hot-encoding,label handel)
        (model_trainer -- here we train the model )
pipeline folder--
        here we will trigger or call all the components----
        (train pipeline--)
        (predict_pipeline--)
logger.py--(it is used for logging)
exception.py--(it is for exception handeling)
utils.py--(to use it in comman way,to read a data from db then can create a mongo client,to save the model in cloud can be done and it can be called inside the components)

---------------------------------
exception.py--start with exception handeling code
logger.py--to show or log to console all the info in some files
--------------------------------------------------------------------------------------------------------------------------
        THIS WAS THE BASIC STRUCTURE TO MAKE THE PROJECT NOW YOU HAVE TO CHOOSE THE WHICH TYPE OF DATA YOU WANT TO USE
notebook (folder)--
        data(folder)--
                EDA.ipynb--for data insights
                model_training.ipynb--for training the model

----------------------------------------------------------------------------------------------------------------------------------------
                       model training is completed so now start the implementation of it

src-
        data_injection.py-(work on it- read the data set from the specific source)
                1. Loading raw data into the pipeline
                2. Validating the input data
                3. Storing the raw data
                4. Splitting data     into-  ( Train set , Test set )
                


