#!/usr/bin/python3

# INET4031
# Your Name: Chi Le
# Data Created: Mar 20, 2025
# Date Last Modified: Mar 25, 2025

import os #This module is for handling the Current Working Directory, creating a Directory, listing out Files and Directories with Python, and deleting Directory or Files using Python.
import re #This module provides regular expression matching operations similar to those found in Perl. It offers functions like search(), match(), findall(), etc.
import sys #This module provides variables for better control over input or output. We can redirect the input and output to other devices. This can be done using three variables - stdin, stdout, and stderr.

def main():
    # Prompt the user to determine if the script should run in dry-run mode.
    dry_run = input("Would you like to run in dry-run mode? (Y/N): ").strip().lower() == 'y'
    
    for line in sys.stdin:
        # Ignore comment lines in the input file, which means lines that start with "#".
        # The regular expression checks if the line starts with "#" to determine if it is a comment.
        match = re.match("^#", line)

        # This splits the input line by colons ":" to extract the users' details.
        fields = line.strip().split(':')

        # The IF statement ensures that the format is correct.
        # The IF statement will skip commented out lines (starting with "#") and lines that do not have exactly 5 fields.
        if match or len(fields) != 5:
            if dry_run:
                print(f"Skipping invalid line: {line.strip()} (Not enough fields or commented out)")
            continue

        # These lines are used to extract user information from fields.
        username = fields[0]   # The username for the new account.
        password = fields[1]   # Password for new account.
        gecos = "%s %s,,," % (fields[3], fields[2])   # Constructing the GECOS (user information) field.

        # Splitting group entries. If there are multiple groups, they are separated by commas.
        groups = fields[4].split(',')

        # Letting the user know about the account creation process.
        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        if dry_run:
            print(f"[DRY-RUN] Command: {cmd}")  # Prints the command instead of running it.
        else:
            os.system(cmd)    # Executes the command to create another user.

        # Informing about setting the password.
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        
        if dry_run:
            print(f"[DRY-RUN] Command: {cmd}")  # Prints the command instead of running it.
        else:
            os.system(cmd)    # Executes the command to set the password.

        for group in groups:
            # The IF statement is looking for the character '-'. If the group is '-', it means the user shouldn't be added to any groups.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                
                if dry_run:
                    print(f"[DRY-RUN] Command: {cmd}")  # Prints the command instead of running it.
                else:
                    os.system(cmd)   # Executes the command to add user to the group.

if __name__ == '__main__':
    main()
