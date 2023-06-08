#       User Management System API


### Priyanshu Vyas
### (vyas.priyanshu23@gmail.com)

Performs CRUD operation in MongoDB using Python and Flask.

## API Endpoints:
* GET ***/alltasks*** -

    Returns all the task


* GET ***/task/:id*** -
 
   Returns a single task by its ID.
   

* POST ***/addtask*** -

   Create a new task in the database.

   _Request Format:_
   ```
    {
        "title": "TASK_TITLE",
        "description": "TASK_DESCRIPTION",
        "due date": "TASK_DUE_DATE",
        "status": "Incomplete OR Completed OR In Progress"
    }
    ```

* PUT ***/updatetask/:id*** -

   Update a task using its ID.
   
   _Request Format:_
   ```
    {
        "title": "UPDATED_TASK_TITLE",
        "description": "UPDATED_TASK_DESCRIPTION",
        "due date": "UPDATED_TASK_DUE_DATE",
        "status": "Incomplete OR Completed OR In Progress"
    }
    ```

* DELETE ***/deletetask/:id*** -

   Delete a task using its ID.
   


### Follow the steps to use this on your machine:

## Cloning the Repo

To get started with this project, follow these steps:

Clone the repository to your local machine:
```
  git clone https://github.com/PriyanshuVyas/UMS-API-python.git
 ```

## Install the dependencies:
```
pip install flask 

pip install pymongo
```

## Start the server:

Run main.py

The default port is 5000.

The server will start running on http://localhost:5000.

## Configuration

The following environment variables can be used to configure the API:

    CONNECTION_URL: MongoDB connection URL.
     
