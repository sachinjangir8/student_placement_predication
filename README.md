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
        when u run it,it will create the --student_placement_predication.egg-info 

