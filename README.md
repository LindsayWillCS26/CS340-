# CS340
About the Project/Project Title
This project provides a custom Python Module (CRUD_Python_Module.py) designed to interface with the Austin Animal Center (AAC) MongoDB database. The module creates a reusable, object-oriented database access layer, allowing software applications to perform database operations freely and smoothly without writing raw data queries directly into the application code. Furthermore, it integrates into an interactive Dash web application dashboard that enables filtering, data viewing, and geolocation mapping for Graziso Salvare rescure animals.

Motivation
The motivation behind this project is to build a scalable, secure, and maintainable backend module for Grazioso Salvare (a software company that trains rescue animals). By capturing the database management and dedicating Python CRUD class, backend developers can easily write, retrieve, and filter shelter animal records while enforcing user security and connection consistency.
Tools and Rationale:
•	MongoDB (The Model): MongoDB was selected as the database component because it is a NoSQL document-based database. The Austin Animal Center dataset features many diverse, sometimes unstructured fields. MongoDB stores data in BSON format (similar to JSON), which then translates effortlessly into the Python dictionaries. This makes passing queried data from the database directly into Pandas DataFrames fast and intuitive.
•	Resource: MongoDB
•	Dash Framework (The View and Controller): The Dash framework by Plotly was used to build the web application. Dash handles both the View (Visual layout, including the HTML/CSS components, data tables and leaflet maps). The callbacks act as the controller by listening for the user inputs (such as clicking the “Water Rescue” radio button), calling the CRUD module to fetch the new data, and then updating the View dynamically without needing to reload the webpage.
•	Resource: Dash by Plotly
•	Steps Teken to Complete the Project
•	Database Initialization: I first configured the local MongoDB environment, imported the AAC shelter outcomes CSV dataset, and then created a secure database user (aacuser).
•	Backend Development: I developed the CRUD_Python_Module to act as the interface between Python and MongoDB, writing discrete methods for Create, Reade, Update, and Delete operations.
•	Frontend Development: I structured the Dash application using Jupyter Notebook, implementing the Grazioso Salvare logo, the interactive filter radio buttons, the Dash Datatable and the Dash Leaflet map.
•	Integration (Callback): Finally, I wrote callback functions to link the frontend components to the backend CRUD module so that the user selections accurately filtered the dataset and updated the table and map simultaneously.

Getting Started
To get local copy of this project up and running in the environment, you must follow these steps:
•	Prerequisites: Ensure Python 3x and MongoDB are installed and running locally on your environment (Or accessible via IDE workspace)
•	Database Setup: Verify that the Austin Animal Center dataset is imported to MongoDB under the aac database and animals collection.
•	Database User Configuration: Create a database user with readWrite access on the aac database using the MongoDB shell:
o	Use aac
Db.creatUser({
    User: “aacuser”,
    Pwd: “password123”,
    Roles: [{ role: “readWrite”, db: “aac” }]
})

Installation
To run and interact with the CRUD Python Module, install the required Python packages and tools
•	Install Python Driver: PyMongo is required for Python to connect and communicate with MongoDB:
o	Pip install pymongo
•	Install JupyterLab/Jupyter Notebook (If running locally): Required to execute and view the interactive test script (.ipynb):
o	Pip install jupyterlab
•	Verify Standard Python Libraries: The module uses standard built in Python libraries (urllib.parse and bson), which are included automatically with standard Python installations.

Usage

Code Example
from CRUD_Python_Module import AnimalShelter

shelter = AnimalShelter(‘aacuser’, ‘password123’)

sample_animal = {
         “animal_id”: “A123456”,
	       “name”: “TestDog”,
	      “animal_type”: “Dog”,
	      “breed”: “Labrador Retriever Mix”,
	      “color”: “Black”,
	      “outcome_type”: “Adoption”
 	}
	
	#1. Test Create Functionality
	Is_created = shelter.create(sample_animal)
	Print(f”Create status: {is_created}”)

	
#2. Test Read Functionality
	Query_result = shelter.read({“name”: “TestDog”})
	Print(f”Query Result Count: {len(query_result)}”)
	Print(query_result)


Tests
To verify that the AnimalShelter class interacts properly with the MongoDB database, automated tests are performed using the provided test script in Jupyter Notebook (ModuleFourTestScript.ipynb) and ProjectTwoDashboard.ipynb

How to Run Tests:
•	Open the ModuleFourTestScript.ipynb file in the IDE environment.
•	Ensure the MongoDB service is active and the aacuser credentials are created in the aac database.
•	Select the test cell and click Run (Or shift + enter) to execute the Python test Script.
Expected Test Output:
•	Create Test: Returns Create Status: True. This confirms the success of insertion into the animals collections
•	Read Test: Returns Query Result Count: 1 and prints a list containing the newly created document dictionary along with its generated ObjectId.
#3, Test Update Functionality
Query = {“animal_id”: “A123456”}
Update_data = {“name”: “UpdatedTestDog”}
Update_count = shelter.update(query, update_data)
Print(f”Update Count: {update_count}”)

	#4 Test Delete Functionality 
		Delete_count = shelter.delete({“animal_id”: “A123456”})
		Print(f”Delete Count: {delete_count}”)
•	Update test: Returns the count of modified documents (Example: Update results count: 1)
•	Delete Test: Returns the count of removed documents (Example: Delete results count: 1) and then shows 0 on final read.
