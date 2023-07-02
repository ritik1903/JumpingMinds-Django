# Elevator problem

### APIs

1. Initialize elevator system
2. Request elevator for floor
3. Get elevator by Id
4. Get all elevators
5. Close elevator door (open by default)

## About this repo
- Every PR sent to main branch and rest framework branch will run tests on pull requests.
- I have set up pre-commit-hooks which would stop the commit if the tests fail.
- Every PR is double verified via `pre-commit-hooks` and `github workflows`.
- The pre-commit hooks also consist of text formatting via `black`

### To checkout the api in action please visit: [https://drive.google.com/file/d/1ObNXuVz7-B_wJYl9TQTnwS3We7ymT9OG/view?usp=sharing](https://drive.google.com/file/d/1ObNXuVz7-B_wJYl9TQTnwS3We7ymT9OG/view?usp=sharing)

## Interactions with the project

- To install all the requirements run
```
pip install -r requirements.txt
```

- To run tests use:
```
python manage.py test
```

- To run the server use:
```
python manage.py runserver
```

## Assumptions (Mentioned in requirements)

1. Number of elevators in the system will be defined by the API to initialize the elevator system
2. Elevator System has got only one button per floor.
3. So if there are a total of 5 floors, there will be 5 buttons per floor.
4. Note that, this doesn't not mimic real world, when you would have a total of 10 buttons for 5 floors ( one for up and one for down)
5. Once the elevator reaches its called point, then based on what floor is requested, it moves either up or down.
6. Assume the API calls which makes elevator go up/down or stop will reflect immediately. When the API to go up is called, you can assume that the elevator has already reached above floor.
7. The system has to assign the most optimal elevator to the user according to their request.

**I have assumed infinite number of floors, It can be limited if required**

### Available schema
- Lift: [Check here](./data_models/lift.md)
- Requests_per_lift: [Check here](./data_models/Requests_per_lift.md)
### Available routes:

- `/` : [Contracts](./apiContracts/list-all-lifts.md)
- `create/?count=<number>`: [Contracts](./apiContracts/create-lifts.md)
- `move/?floor=<number>`: [Contracts](./apiContracts/move-lift.md)
- `ooo/?lift=<number>`: [Contracts](./apiContracts/mark-ooo.md)
- `history/?lift=<number>`: [Contracts](./apiContracts/lift-history.md)
- `door/?lift=<number>`: [Contracts](./apiContracts//toggle-door.md)

### Interpretations

- Initialize the elevator system to create ‘n’ elevators in the system
  - Create an api that takes in a number `n` and generates `n` lifts

- Fetch all requests for a given elevator
  - create an api that accepts a number and returns all the requests sent to the specified lift

- Fetch the next destination floor for a given elevator
  - based on the assumption number 6 this is handled by the move api

- Fetch if the elevator is moving up or down currently
  - based on the assumption number 6 this is handled by the move api by changing move_up flag in the lift schema

- Saves user request to the list of requests for a elevator
  - Save all the user interactions coming to all the api's

- Mark a elevator as not working or in maintenance
  - Create an api that accepts a lift number and marks that lift in maintenance and thus this lift will become non functional.

- Open/close the door
  - Create an api that accepts the lift number as parameter and toggles the door_open flag of the lift schema
