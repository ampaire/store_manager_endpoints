#STORE MANAGER ENDPOINTS 
[![Coverage Status](https://coveralls.io/repos/github/ampaire/store_manager_endpoints/badge.svg?branch=master)](https://coveralls.io/github/ampaire/store_manager_endpoints?branch=master)
[![Build Status](https://travis-ci.org/ampaire/Api.svg?branch=master)](https://travis-ci.org/ampaire/Api)


Store manager is an application that enables users to keep track of goods in their stores. It is meant for managerial purposes by store owners. The two major people that operate it are the admins who add store attendants and can choose to make them administrators.


##GETTING STARTED
* Fork into my repository by running `$git clone https://github.com/ampaire/store_manager_endpoints`
* Creating project path `$cd store_manager_endpoints`
* Creating a virtual environment  `$virtual env venv -p python3`
* Activating the virtual environment  linux - `$source venv/bin/activate` and windows `c:/ .\venv\Scripts\activate venv/bin/activate`
* `$pip install -r requirements.txt`  for the project dependences

###Required
    * pip3
    * pylint
    * pytest
    * flask
    * python 3
    * requests
    
##Installation
    all required modules listed above need to be installed 
* all installations are run with $pip install module
Example
`$pip install pytest`

##Usage
```
@app.route("/api/v1/<examples/example>", methods=["?"]) "specifies the route for the api"
```

##Development
```
$virtual env venv
$source venv/bin/activate
$pip install flask
$pip install requests
$pip install pytest
```
####endpoints 
Method                   |endpoint(s)
-------------------------|----------------------------
GET(gets all products)   |api/v1/products
-------------------------|............................
GET(gets one product)    |api/v1/products/<int:id_>
-------------------------|----------------------------
GET(gets all sale orders)|api/v1/sales                   
-------------------------|----------------------------
POST(adds a sale order)  |api/v1/sales
-------------------------|----------------------------
POST(adds a product)     |api/v1/products
-------------------------|----------------------------
PUT(modifies a product)  |api/v1/products/<int:id_>
-------------------------|----------------------------
DELETE(deletes a product)|api/v1/products/<int:id_>
-------------------------|----------------------------

###Deployment
This app has been hosted on Heroku at https://phestores.herokuapp.com/

###Contributing
To contribute to this project,
- fork this repository and make necessary changes. Then create a branch `improved-feature` and commit changes

###AUTHOR
    Ampaire Phemia



This repository mainly is for creating endpoints for the products in the store. The main endpoints that I created were:
- An admin can create/add a product
- An admin can modify a product
- An admin can delete a product
- A store attendant/ admin can get all the products in the store
- An admin can get all sale orders
- A store attendant can create a sale order
- An admin/ store attendant can get a specific product in the store

#GETTING STARTED
It was a project that required one to use a data structure to implement the endpoints and not a data structure.
So to begin with; 
- You need to be having knowledge of Git, Python and the you are good to go.
- You need to be having a text editor installed on your computer for example Visual Studio Code

#Installation
Open your favorite Editor and in the terminal run the following command
#$pip install virtualenv

It is always good to work in the virtual environment and if you do not have pip installed you could install it first before installing virtualenv. When you are done installing the virtual env run
#$virtualenv venv
and then 
#$source venv/bin/ctivate
for those using linux to activate the virtual environment.
Run
 #$pip install --user flask 
 to install flask that we are going to use in building our application
 #$pip install requests
 since for data structures we request JSON to get our data
 #$pip install pylint
 to help in organising/autoformatting our wok.

 For the tests I installed pytest
 #$pip install pytest.

 And finally install requirements.txt by running
 #$pip install -r requirements.txt

 #Running the app
 -the app is run using $python3 run.py

 #Testing
 - you run $pytest-v

The created app can help one to -add a new product, get all products, modify an existing product, delete a produxt, create a sale order, get all sale orders and to get one product from a group of products




 
