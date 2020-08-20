# Python Assignment

This is my Python assignment to build a mini HR system, updated with HTTP implementation. 

**Requirements**

Only cover basic requirements, which are:
1. Login/Logout
    - Check if user exist or not
    - If wrong email/password, will go back to main menu
3. View Employee
    - Data already formatted properly, includes using config variable that has been provided
    - Based on role, validation already added from menu that available to display for spesific roles
        - Staff : can only view self data
        - Manager : can view team data including self data
        - Administrator : can view all employee data
4. Apply Leave
    - Default value for all employees: 14 days leave balance
    - System can automatically rejects if user don't follow these rules:
        - Leave cannot be applied during peak period (7.7, 8.8, 9.9, 10.10, 11.11, 12.12)
        - Everybody in team cannot be on leave together (exclude manager)
    - Special rule for manager, manager can take leave anytime except peak period (cos he is the BOSS)
    - Weekend won't be counted as leave
    - Leave taken on Public Holidays won't be counted (31-July, 10-Aug, 16-Nov, 25-Dec)
    - Balance will be deducted immediately after apply leave
4. Approve Leave and Add Employee
    N/A (not covered for HTTP implementation)

**Others**

## Installation
1. Clone this repo.  

2. Create a virtualenv in the root dir of the cloned repo.  
**Note**: ```pip install virtualenv``` if command is not found in your terminal.
    ```sh
    # For Python 2
    virtualenv venv
    # For Python 3
    python3 -m venv venv
    ```
3. Activate the virtualenv created in the previous step.  
**Note**: You can configure Pycharm to set this virtualenv as the python interpreter.  
```source venv/bin/activate```

4. Install lib via requirements.  
    ```sh
    # For Python 2
    pip install -r requirements.txt
    # For Python 3
    pip3 install -r requirements.txt
    ```
## Run the client and server
1. To run the client.  
```sh client.sh```

2. To run the server.  
```sh server.sh```