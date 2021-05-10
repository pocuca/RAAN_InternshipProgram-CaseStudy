**RAAN Internship Program Case Study**


This case study is the first stage of the recruitment process for Advanced analytics internship position at Roche.

The web app is deployed to the Heroku host service and can be found on the following link:

* https://bojana-roche-app.herokuapp.com

The graphs were done using _Cytoscape Dash_ library, and the data source is a directed graph from the provided file data. The edge width is proportional to the weight of the edges. The node size on the plots is proportional to the 'importance' of the person and was done using Page Rank. 

First, the virtual environment needs to be created in the following way:

* python -m venv my_env

To activate the environment do the following:

* source my_env/bin/activate

Next, to install all the required libraries and tools do: 
* pip install -r requirements.txt

The case study data is omitted from this Github project. In order for this project to work, the data needs to be placed in the _data_ folder.

And finally, to start the project, one needs to run the _app.py_ file from the src folder. The web app will open in the local web browser.


   
