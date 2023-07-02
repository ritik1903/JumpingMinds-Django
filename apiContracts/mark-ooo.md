# Contract for: Marking a lift OOO

- **Route**: `ooo/`
- **Params**: `lift = <lift_number >`
- **Method**: `GET`

# Description

- This Route marks the desired lift out of order
- when this api is called again with same number it marks the lift active.
- This Route accepts a query param of lift having an integer value.
- (the lift_number here is not the id of the lift its similar to shutting down the third lift)
- If no parameter is passed, a response of lift does exist is not generated

**Response schema**

- Success

```
{
    "id": Lift Id,
    "current_floor": floor on which the lift is present,
    "move_up": boolean field for checking if lift moved up or down,
    "door_open": boolean field for checking if lift doors are open or close,
    "busy": boolean field for checking if lift is busy or free,
    "is_OOO": boolean field for checking if lift is in maintenance
}
```

# Image gallery

- ![image](https://user-images.githubusercontent.com/57758447/222747772-8c107d82-0965-454f-b69a-cf4cc8839753.png)
