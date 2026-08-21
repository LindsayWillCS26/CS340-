# CS340
About the Project/Project Title
This project provides a custom Python Module (CRUD_Python_Module.py) designed to interface with the Austin Animal Center (AAC) MongoDB database. The module creates a reusable, object-oriented database access layer, allowing software applications to perform database operations freely and smoothly without writing raw data queries directly into the application code. Furthermore, it integrates into an interactive Dash web application dashboard that enables filtering, data viewing, and geolocation mapping for Grazioso Salvare rescue animals.

Motivation
The motivation behind this project is to build a scalable, secure, and maintainable backend module for Grazioso Salvare (a software company that trains rescue animals). By capturing the database management and dedicating Python CRUD class, backend developers can easily write, retrieve, and filter shelter animal records while enforcing user security and connection consistency.
Tools and Rationale:
•	MongoDB (The Model): MongoDB was selected as the database component because it is a NoSQL document-based database. The Austin Animal Center dataset features many diverse, sometimes unstructured fields. MongoDB stores data in BSON format (similar to JSON), which then translates effortlessly into Python dictionaries. This makes passing queried data from the database directly into Pandas DataFrames fast and intuitive.
•	Resource: MongoDB
•	Dash Framework (The View and Controller): The Dash framework by Plotly was used to build the web application. Dash handles both the View (Visual layout, including the HTML/CSS components, data tables, and Leaflet maps). The callbacks act as the controller by listening for the user inputs (such as clicking the “Water Rescue” radio button), calling the CRUD module to fetch the new data, and then updating the View dynamically without needing to reload the webpage.

How do you write programs that are maintainable, readable, and adaptable?
-The separation of concerns: Keeps the raw MongoDB queries abstracted inside the CRUD_Python_Module.py class. The Dash application should only call high-level class methods (e.g. create(), read() rather than executing raw PyMongo queries directly within UI callback functions.
-Docstrings and Type Hints: Explicitly documented sturctures and so the query returns the formats for future developers to call methods easily and cleanly
-Modular code structure: Grouping the functional responsibilities logically then helps the databases connect logicaly; CRUD operations and error handling live in the module, UI layout, and callbacks in the Dash dashboard app.

Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?


How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?
What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?                                                                                             
