# INET4031 - Module 8 - Automating User Management


## Program Description

Manually managing user accounts in Linux can be time-consuming, error-prone, especially when handling multiple users. This useful Python script makes managing users in Linux automatic by reading user details from an input file and executing necessary commands to create users and assign them to groups. 

If a system administrator add an user manually, they would need to use the 'adduser' command. Then, they would need to add user first name, last name, group, and every information manually. With this Python script, the process is automated to save time, reduce errors, and ensure consistency in the process.
  
##  Program User Operation

This section provides an overview of how the script operates and how the user can execute it:

### Input File Format

The input file follow a structured format: 
*username:password:last_name:first_name:group*
**username** - The login name for the user.
**password** - The login password for the user.
**last_name** - The user's last name.
**first_name** - The user's first name.
**group** - The groups that the user should be added to. If no group is specified, the user is created without any group assignment.

**Skipping a line:** To prevent a line from being processed, put a '#' in the beginning of the line of code (comment it out). 

**Assign user to no groups:** If a user do not belong to any group, leave a '-' in the space of the group field.

### Command Excuction

**To execute the scrip**t, ensure Python is installed and the script is executable:
`chmod a+x create-users.py`

**To run the script, use:**
`./create-users.py < create-users.input`

**or use Python explicitly:**
`sudo python create-users.py < create-users.input`
(use `sudo python3 create-users.py < create-users.input` if Python 3 is installed)

### "Dry Run"

A dry run is ran to ensure the code works with no errors without actually creating users in the system. To able a dry run, comment out the print(cmd) and os.system(cmd) statements in the script.

`#print(cmd)  # Uncomment this to preview commands
#os.system(cmd)  # Comment this out to prevent execution`

When executed in this mode, the script will display the commands it would run but will not create any users or modify the system. 
