# STORE MANAGER ENDPOINTS 
[![Coverage Status](https://coveralls.io/repos/github/ampaire/store_manager_endpoints/badge.svg?branch=master)](https://coveralls.io/github/ampaire/store_manager_endpoints?branchdevelop)
[![Build Status](https://travis-ci.org/ampaire/store_manager_endpoints.svg?branch=develop)](https://travis-ci.org/ampaire/store_manager_endpoints)
<a href="https://codeclimate.com/github/ampaire/store_manager_endpoints/maintainability"><img src="https://api.codeclimate.com/v1/badges/91c97cb448d3dbcfd712/maintainability" /></a>

Store manager is an application that enables users to keep track of goods in their stores. It is meant for managerial purposes by store owners. The two major people that operate it are the admins who add store attendants and can choose to make them administrators. This is the implementation of the API for this project.


## GETTING STARTED
* Fork into my repository by running `$git clone https://github.com/ampaire/store_manager_endpoints`
* Creating project path `$cd store_manager_endpoints`
* Creating a virtual environment  `$virtual env venv -p python`
* Activating the virtual environment  linux - `$source venv/bin/activate` and windows `c:/ .\venv\Scripts\activate venv/bin/activate`
* `$pip install -r requirements.txt`  for the project dependences.

### Prerequisites

    * pip3
    * pylint
    * pytest
    * flask
    * python 3
    * requests
    
## Installation.
      all required modules listed above need to be installed 
* all installations are run with `$pip install <module-name>`
Example
`$pip install pytest`


## Development
```
$virtual env venv
$source venv/bin/activate
$pip install flask
$pip install requests
$pip install pytest
```
## Usage
```
@app.route("/api/v1/<examples/example>", methods=["?"]) "specifies the route for the api"
```

#### endpoints 
Method                   |endpoint
-------------------------|-----------------------------
GET(gets all products)   |api/v1/products
-------------------------|-----------------------------
GET(gets one product)    |api/v1/products/<int:id_>
-------------------------|-----------------------------
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

### Running
`$python run.py`

### Testing
To run the tests 
`$pytest

### Contributing
To contribute to this project,
- fork this repository and make necessary changes. Then create a branch `improved-feature` and commit changes

### AUTHOR
    [Ampaire Phemia](github.com/ampaire)


