from connection import app, collection
import errorHandling
from flask import jsonify, request
from bson import ObjectId
from bson.json_util import dumps

# ----- Display ALL Tasks ---------
@app.route('/alltasks', methods=['GET'])
def displayAllTask():
    if request.method == 'GET':
        tasks = collection.find()
        res = dumps(tasks)
        return res
    return errorHandling.bad_request()


#------ Display one Task by ID -----
@app.route('/task/<id>', methods=['GET'])
def displayTask(id):
    if id and request.method == 'GET':
        task = collection.find_one({'_id':ObjectId(id)})
        if not task:
            return errorHandling.not_found()
        res = dumps(task)
        return res
    return errorHandling.bad_request()


#---------- Add a Task ----------
@app.route('/addtask', methods=['POST'])
def addTask():
    _data = request.json
    
    _title = _data['title']
    _desc = _data['description']
    _date = _data['due date']
    _status = _data['status']

    if _title and _date and _desc and _status and request.method == 'POST':
        task_data = {
            "title": _title,
            "description": _desc,
            "due date": _date,
            "status": _status
        }
        result = collection.insert_one(task_data)  

        if result.inserted_id:
            res = jsonify(message="Task added successfully")
            res.status_code = 200
            return res
        else:
            return errorHandling.server_error()
    else:
        return errorHandling.bad_request()


#-------- Update a Task --------
@app.route('/updatetask/<id>', methods=['PUT'])
def updateTask(id):
    _data = request.json
    
    _title = _data['title']
    _desc = _data['description']
    _date = _data['due date']
    _status = _data['status']

    if _title and _date and _desc and _status and request.method == 'PUT':
        task_data = {
            "title": _title,
            "description": _desc,
            "due date": _date,
            "status": _status
        }
        result = collection.find_one_and_update({'_id':ObjectId(id)},{'$set':task_data})  

        if result:
            res = jsonify(message="Task updated successfully")
            res.status_code = 200
            return res
        else:
            return errorHandling.not_found()
    else:
        return errorHandling.bad_request()
    

#--------- Delete a Task --------
@app.route('/deletetask/<id>', methods=['DELETE'])
def deleteTask(id):
    if id and request.method == 'DELETE':
        collection.find_one_and_delete({'_id':ObjectId(id)})
        res = jsonify("Task Deleted")
        res.status_code = 200
        return res
    return errorHandling.bad_request()


if __name__ == "__main__":
    app.run(debug=True)

