import requests
import uuid
#https://todo.pixegami.io/docs
ENDPOINT= "https://todo.pixegami.io/"

# case0 test if api work or not
# def test_can_Call_endpoint():
#     response=requests.get(ENDPOINT)
#     assert response.status_code == 200

#CASE1
def test_can_create_task_old():
    #using put method
    #copy the json code and paste below 
    payload={
        "content": "my test content",
        "user_id": "test_user",
        "task_id": "task_task_id",
        "is_done": False,
    }
    create_task_response = requests.put(ENDPOINT + "/create-task", json=payload)
    assert create_task_response.status_code == 200
    data=create_task_response.json()
    print(data)

def test_can_create_task():
   
    #comment below write into helper function 
    # payload={
    #     "content": "my test content",
    #     "user_id": "test_user",
    #     "task_id": "task_task_id", #remove this will genrate by server
    #     "is_done": False,
    # }

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
def test_can_update_task_old():
    #create a task
    payload=new_task_payload()
    assert create_task_response.status_code==200
    create_task_response=create_task(payload)
    task_id=create_task_response.json()["task"]["task_id"]
    #update the task
    new_payload={
        "user_id":payload["user_id"],
        "task_id": task_id,
        "content":"my update content",
        "is_done": True,    
        }
    update_task_response=update_task(new_payload)
    assert update_task_response.status_code==200
    get_task_response=get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data=get_task_response.json()
    assert get_task_data["content"]==new_payload["content"]
    assert get_task_data["is_done"]==new_payload["is_done"]

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

#CASE3 LIST TASK_ID   
def test_can_list_tasks_old():
   #create N tasks
    for _ in range(3):
        payload = new_task_payload()
        create_task_response=create_task(payload)
        assert create_task_response.status_code==200
    list_task_response = list_tasks("test_user")
    assert list_task_response.status_code==200
    data= list_task_response.json()
    print(data)

def test_can_list_tasks():
   #create N tasks
    n=3
    #only generate payload once, generate once with only one user_id
    payload = new_task_payload()
    for _ in range(n):
        create_task_response=create_task(payload)
        assert create_task_response.status_code==200
    #list tasks and check that there are N items
    user_id=payload["user_id"]
    list_task_response = list_tasks(user_id)

    assert list_task_response.status_code==200
    data = list_task_response.json()
    tasks=data['tasks']
    assert len(tasks)==n
    #print(data)

    
 #case4 delete task
def test_can_delete_tasks():
    #create a task
    payload=new_task_payload()
    #create_task_response=requests.put(ENDPOINT + "/create-task", json=payload)
    create_task_response=create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]
    #delete the task
    delete_task_response=delete_task(task_id)
    assert delete_task_response.status_code==200
    # get the task and  check that it's not found
    get_task_response=get_task(task_id)
    #print(get_task_response.status_code) #404 mean not found
    assert get_task_response.status_code

############################
def create_task(payload):
    return requests.put(ENDPOINT + "/create-task", json=payload)
      
def get_task(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")

def new_task_payload():
    #limitation add uuid 
    user_id=f"test_user_{uuid.uuid4().hex}"
    content=f"test_content_{uuid.uuid4().hex}"
    #there are 5 version, 4 version is enough, and it's an object
    #print generate uuid's userid and content
    #print(f"creating task for user {user_id} with content {content}")

    return  {  
        #"content": "my test content",
        "content": content,
        "user_id": user_id,
        "is_done": False,
  }

def update_task(payload):
    return requests.put(ENDPOINT + "/update-task", json=payload)

def list_tasks(user_id):
    return requests.get(ENDPOINT + f"/list-tasks/{user_id}")

def delete_task(task_id):
    return requests.delete(ENDPOINT + f"/delete-task/{task_id}")