# Contract for: Move Lift

- **Route**: `create/`
- **Params**: `floor = <number >`
- **Method**: `GET`

# Description

- This Route moves closest lift to the desired floor
- This Route accepts a query param of floor having an integer value.
- If no Parameter is passed it calls a lift to first floor.

**Response schema**

```
{
    id: id of the lift moved,
    current_floor: Current floor on which the lift is (after moving),
    move_up: A boolean value when false means lift moved down,
    busy: A boolean value when true means lift is in use,
    is_OOO: A boolean field marks lifts under maintenance and active,
    door_open: A boolean value that indicates the state of door
}
```

# Image gallery

- ![image](https://user-images.githubusercontent.com/57758447/222747885-cab85df8-1006-4bce-829c-6e945da61c46.png)
