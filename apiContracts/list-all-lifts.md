# Contract for: List All lifts

- **Route**: `/`
- **Params**: none
- **Method**: `GET`

# Description

- This Route returns an object with all the lifts and their details.(state)
- Any Parameter Passed to this route via queryparams will be ignored

**Response schema**

```
[
    {
        "id": Lift Id,
        "current_floor": floor on which the lift is present,
        "move_up": boolean field for checking if lift moved up or down,
        "door_open": boolean field for checking if lift doors are open or close,
        "busy": boolean field for checking if lift is busy or free,
        "is_OOO": boolean field for checking if lift is in maintenance
    },
]
```

# Image gallery

- ![image](https://user-images.githubusercontent.com/57758447/222747651-445927f4-54df-4f64-9b25-60b1c2a09ac4.png)
