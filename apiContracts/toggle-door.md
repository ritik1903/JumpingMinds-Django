# Contract for: Marking a lift OOO

- **Route**: `door/`
- **Params**: `lift = <lift_number >`
- **Method**: `GET`

# Description

- This api changes the property of door_open for specified lift.
- you can specify the lift by passing in a query parameter of lift
- In case you enter the number mort than the count of lifts available api returns a message of lift not found

**Response Schema**

- Success

```
{
    id: id of the lift moved,
    current_floor: Current floor on which the lift is (after moving),
    move_up: A boolean value when false means lift moved down,
    busy: A boolean value when true means lift is in use,
    is_OOO: A boolean field marks lifts under maintenance and active,
    door_open: A boolean value that indicates the state of door,
}
```

# Image gallery

- ![image](https://user-images.githubusercontent.com/57758447/222748033-ceadac92-a007-4ff3-83e6-100f543f51ad.png)
