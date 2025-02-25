#python -m uvicorn main:app --reload


#definations
from fastapi import APIRouter,HTTPException,FastAPI  #Exception rise pandradhuku import pnnnanum
from pydantic import BaseModel 
 #base modelngra pakage ahh pydantic library lendu import paniruka  
#[pydantic] data format correct-a irukka nu confirm panna oru tool mathiri nadikkum.

app = FastAPI()
router=APIRouter() #oru instance create paniyachu
#(why create instance)
#Class methods and variables use panna.
#Unique data store panna.

tasks=[] #idhu task management so create

class Task(BaseModel):  #Base model .idha pydantic laendu import pannanum
    id:int
    title : str
    description: str  #oru task la mandetorya irukkura fields


#####  get all the tasks  #####


#router instance use pandro
@router.get('/tasks')  #It's a decorator used in FastAPI./tasks endpoint-ku request vandha, this function will handle it.
def get_tasks():
    if not tasks: #tasks illana 
        raise HTTPException(status_code=404,detail="your tasks not found")
    return tasks #get na adha return pandra

#####  id ya vachi tasks ahh get pandradhukku  #####





@router.get('/tasks/{task_id}') #User URL-la oru value pass panna, adha eduthukittu function work pannum.,Example: /tasks/1 nu sonna, task_id = 1.
def get_tasks_by_id(task_id:int): #task_id nu oru parameter.  #: int na integer value expect pannum.
    """
    This function creates new tasks
    """
    for task in tasks:
        if task.id==task_id:
            return task   
    raise HTTPException(status_code=404,detail="not found")

#####  data va create pannikiradhukku  #####


@router.post('/tasks') #task post pandradhukana function 
def create_task(task:Task): #:Task User-defined Pydantic model (data validation panna use pannum).
    tasks.append(task)
    return task


#####  task delete pandradhuku  #####

@router.delete('/task/{task_id}')
def delete_task(task_id:int):
    for index,task in enumerate(tasks): #enumerate using for index edhulendu start aganumnstau easy sollikala.
        if task.id==task_id:
            tasks.pop(index)
            return {"message :" "task deleted sussecfully "}
    raise HTTPException(status_code=404,detail="the task not found")

## put data ##

@router.put('/task/{task_id}')
def update_task(task_id:int ,new_task:Task):
    for index,task in enumerate(tasks): 
        if task.id == task_id:
            tasks[index] = new_task

            return ("MEssage : new task updayted")
    HTTPException(status_code=404,detail="the task not found")


            













