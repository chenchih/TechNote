import requests
#https://todo.pixegami.io/docs
ENDPOINT= "https://todo.pixegami.io/"

def test_can_Call_endpoint():
    response=requests.get(ENDPOINT)
    assert response.status_code == 200

#CASE1
def test_can_create_task():
    #Step1
    payload=new_task_payload()
    #create_task_response = requests.put(ENDPOINT + "/create-task", json=payload)
    create_task_response=create_task(payload)
    assert create_task_response.status_code == 200
    data=create_task_response.json()
    #print(data)

    #step2
    #get task_id
    task_id=data["task"]["task_id"]
    #get_task_response = requests.get(ENDPOINT + f"/get-task/{task_id}")
    get_task_response=get_task(task_id)
    assert get_task_response.status_code==200
    get_task_data=get_task_response.json() #get value 

    #Step3 check data 
    assert get_task_data["content"]==payload["content"]
    # assert get_task_data["user_id"]=="other content " #let it fail
    assert get_task_data["user_id"]==payload["user_id"]

    #print(data["task"]["task_id"])

#CASE2
def test_can_update_task():
    #create a task
    payload=new_task_payload()
    create_task_response=create_task(payload)
   
    assert create_task_response.status_code==200
    task_id=create_task_response.json()["task"]["task_id"]
    #print("Case2:create task")
    #print(create_task_response.json())
    #update the task
    new_payload={
        "user_id":payload["user_id"],
        "task_id": task_id,
        "content":"my update content",
        "is_done": True,    
        }
    update_task_response=update_task(new_payload)
    assert update_task_response.status_code==200
    # get and validate thje changes
    get_task_response=get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data=get_task_response.json()
    #print("Case2:update task")
    #print(get_task_data)
    assert get_task_data["content"]==new_payload["content"]
    assert get_task_data["is_done"]==new_payload["is_done"]

    
############################
def create_task(payload):
    return requests.put(ENDPOINT + "/create-task", json=payload)
      
def get_task(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")

def new_task_payload():
    return  {  
        "content": "my test content",
        "user_id": "test_user",
        "is_done": False,
  }
def update_task(payload):
    return requests.put(ENDPOINT + "/update-task", json=payload)