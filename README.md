# Python Assignment

This is my Python assignment to build a mini HR system. 

**Requirements**

Only cover basic requirements, which are:
1. Login/Logout
    - Check if user exist or not
    - If wrong email/password, will go back to main menu
2. Add Employee
    N/A
    - Data already formatted properly, includes using config variable that has been provided
    - Based on role, validation already added from menu that available to display for spesific roles
        - Staff : can only view self data
        - Manager : can view team data including self data
        - Administrator : can view all employee data
3. Apply Leave
    - Default value for all employees: 14 days leave balance
    - System can automatically rejects if user don't follow these rules:
        - Leave cannot be applied during peak period (7.7, 8.8, 9.9, 10.10, 11.11, 12.12)
        - Everybody in team cannot be on leave together (exclude manager)
    - Special rule for manager, manager can take leave anytime except peak period (cos he is the BOSS)
    - Weekend won't be counted as leave
    - Leave taken on Public Holidays won't be counted (31-July, 10-Aug, 16-Nov, 25-Dec)
    - Balance will be deducted immediately after apply leave
4. Approve Leave
    N/A

**Others**

- Run the program from the Main.py
- Program will loop until user manually exit
- Currently there is no different employee status, all considered as permanent employee
- Admin doesn't support apply and approve leave