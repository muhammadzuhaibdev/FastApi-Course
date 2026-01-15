from fastapi import FastAPI
import uvicorn
app = FastAPI()

studentsList = [
    {"id": 1 , "name":"Zuhaib", "email":"zuhaib@gmail.com", "phone": "03267127657"},
    {"id": 2 , "name":"Hamza", "email":"hamza@gmail.com", "phone": "03287225203"},
]

@app.get('/getStudentsList/{password}')
def getStudentsList(password):
    print('Get Students List Api Called')
    if not password:
        return "Password is required"
    elif not password == 'Pakistanzindabad':
        return 'Password is wrong'   
    elif password == 'Pakistanzindabad':
        return studentsList
    
@app.post('/createStudent')
def createStudent(userName:str, email:str,phone:str):
    print('Create User Api Called')
    for studentData in studentsList:
        if studentData["email"] == email:
            return 'User Already Exist'
    else:
        studentsList.append({"id": len(studentsList) + 1, "userName": userName, "email":email, "phone":phone})
        return studentsList
    
@app.put('/updateUser/')
def updateUser(id:str, userName:str):
    if not id: return 'Id is required'
    if not userName: return "Updated UserName is required"
    
    global studentsList
    def updatedFunc(student):
        if student["id"] == int(id):
            return {**student, "name":userName}
        else:
            return student

    studentsList = list(map(updatedFunc,studentsList))
    return studentsList


    
@app.delete('/deleteUser/')
def deleteUser(id):
    if not id: return "Id is required"
    
    global studentsList
    
    # def abc(student):
    #     return not student["id"] == int(id)
    # studentsList = list(filter(abc,studentsList))

    studentsList = list(filter(lambda s:  not s["id"] == int(id), studentsList))        
    print(studentsList)
    return studentsList


def start():
    uvicorn.run('student_app.main:app',host='127.0.0.1',port=8080,reload=True)