## Test Case Description

This is a good practice for learning how to use the RestAPI automation test.This YouTube tutorial teaches a great concept on it. Please refer to my Python code, I will keep you updated if there are some notes in advance. `2024 June`

- **TestCase1** :Testing the Create() endpoint
- **TestCase2 :** Testing the Update() endpoint
- **TestCase3:** Testing the List() endpoint with unique users
- **TestCase4:** Testing the Delete() endpoint

> Summary of each code cheatsheet:

- create a task: `requests.put(ENDPOINT + "/create-task", json=payload)`
- send request: `create_task_response=create_task(payload) `
- check server status: `assert create_task_response.status_code==200`
- update task: `requests.put(ENDPOINT + "/update-task", json=payload)`
- delete task:`requests.delete(ENDPOINT + f"/delete-task/{task_id}")`
- list task: `requests.get(ENDPOINT + f"/list-tasks/{user_id}")`
- get task_id: `create_task_response.json()["task"]["task_id"]`

### Status Update

- `20240628`: initial add the code learn from youtube
  - add the full code
  - add a draft code for some debug
- add a draft file, for original code, before refactoring code

## Python Libary:

`requests`
`pytest`

## Reference:

- [Youtube Video ](https://www.youtube.com/watch?v=7dgQRVqF1N0&t=1434s)
- [Github from author](https://github.com/pixegami)

## API URL:

- test endpoint: `https://todo.pixegami.io/`
- UI interface: `https://todo.pixegami.io/docs`

## Command and Note:

### How to run test suite with pytest

in `pytest` it will only run the function that start with `test\_`,

> - run all the test suite, all function name conventions with `test` . It will treate it as test case, and you can use this to run all testcase. `pytest <testscript.py>`

> - run specfic test suite or function
>   `pytest -v -s  <testscript.py>::<test function name>`

### Pytest some option to use

- `-m`: if pytest run error, please use `python3 -m`. It means import a module _or package_ for you, then run it as a script.
- `-v`: verbose, print more information pass or fail
- `-s`: show output, like print

### How to run this code:

- Run all test suite(all test case)

```
pytest .\test_tofo_api.py -v -s
```

- Run spefic test case:

```
pytest -v -s .\test_tofo_api.py::test_can_delete_tasks
```

![Screenshot](RestAPI_Screenshot.png)
