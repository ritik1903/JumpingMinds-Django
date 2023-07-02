# Contract for: Getting user interactions on a lift

- **Route**: `history/`
- **Params**: `lift = <lift_number >`
- **Method**: `GET`

# Description

- This API gets all the user interaction for the specified lift
- You can specify the lift number by passing the query parameter of lift
- In case there is no parameter specified the api returns the history of the first lift
- The api will return an error if the number for lift parameter exceeds the count of lifts present.

**Response Schema**

- Success

```
{
    "Lift_id": Id of the selected lift,
    "history": [] list of user interactions in the form of string
}
```

# Image gallery

- ![image](https://user-images.githubusercontent.com/57758447/222747456-770a9903-cb29-46fb-b490-7518370c2571.png)
