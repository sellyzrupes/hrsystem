# Python Assignment

This is my Python assignment to build a mini HR system. 

**Requirements**

Only cover basic requirements, which are:
1. Login/Logout
    - Check if user exist or not
    - If wrong email/password, will go back to main menu
2. Add Employee
    - Before admin input team_id and role_id, system will print out all available team_id and role_id
3. View Employee
    - Data already formatted properly
    - Based on role, validation already added from menu that available to display for spesific roles
        - Staff : can only view self data
        - Manager : can view team data including self data
        - Administrator : can view all employee data
4. Apply Leave
    - Default value for all employees: 14 days leave balance
    - System can automatically rejects if user don't follow these rules:
        - Only can apply from current date until end of 2020
        - Leave cannot be applied during peak period (7.7, 8.8, 9.9, 10.10, 11.11, 12.12)
        - Everybody in team cannot be on leave together (exclude manager)
        - Not enough leave balance
    - Special rule for manager, manager can take leave anytime except peak period (cos he is the BOSS)
    - Weekend won't be counted as leave (not yet added)
    - Leave taken on Public Holidays won't be counted (31-July, 10-Aug, 16-Nov, 25-Dec)
    - Balance will be deducted immediately after apply leave
    - User cannot apply 2 leaves at the same time, need to wait for first leave to be approved
4. Approve Leave
    - Manager can approve or reject staff leave
    - System will only show pending leave to manager
    - If manager rejects, balance need to be returned
    - For now no need Admin approval if manager takes leave, later if have time need to add Admin Approval

Other things to note:
- Program will loop until user manually exit
- Currently there is no different employee status, all considered as permanent employee
- Admin don't support apply and approve leave

**Others**

Run the program from the Main.py