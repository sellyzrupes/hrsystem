# Python Assignment

This is my Python assignment to build a mini HR system. 

**Requirements**

Only cover basic requirements, which are:
1. Login/Logout
    - Check if user exist or not
    - If wrong email/password, will go back to main menu
2. Add Employee
    - Email format validation (not yet added)
    - Before admin input team_id and role_id, system will print out all available team_id and role_id (not yet added)
    - Check if team_id not exist (not yet added)
    - Check if role_id not exist (not yet added)
3. View Employee
    - Data already formatted properly
    - Based on role, validation already added from menu that available to display for spesific roles
        - Staff : can only view self data
        - Manager : can view team data including self data
        - Administrator : can view all employee data
4. Apply Leave
    - Default value for all employees: 14 days leave balance
    - System can automatically rejects if user don't follow these rules:
        - Leave applied during peak period
        - Everybody in team on leave (exclude manager)
        - Not enough leave balance
    - Special rule for manager, manager can take leave anytime except peak period (cos he is the BOSS)
    - Weekend won't be counted as leave (not yet added)
    - Balance will be deducted immediately after apply leave
4. Approve Leave
    - Manager can approve or reject staff leave
    - If manager rejects, balance need to be returned
    - For now no need Admin approval if manager takes leave, later if have time need to add Admin Approval

Other things to note:
- Program will loop until user manually exit
- Currently there is no different employee status, all considered as permanent employee
- Admin don't support apply and approve leave

**Others**

Run the program from the Main.py