# Contract for: Create Lifts

- **Route**: `create/`
- **Params**: `count = <number >`
- **Method**: `GET`

# Description

- This Route creates multiple lifts when called.
- This Route accepts a query param of count having an integer value.
- If no Parameter is passed it creates 0 lifts.

**Response schema**

```
{
    "message": "All Lifts created successfully",
    "Total_count": total count of the lifts present,
    "Created_count": count of the lifts created
}
```

# Image gallery

- ![image](https://user-images.githubusercontent.com/57758447/222747255-4471255d-f6b6-438f-a64e-73512065084c.png)
