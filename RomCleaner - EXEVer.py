import glob
import os
import click


def remove_string_from_file_name(file_path, string_to_remove, dry_run=False):
    path, file_name = os.path.split(file_path)
    new_name = file_name.replace(string_to_remove, '')
    new_path = os.path.join(path, new_name)
    if dry_run:
        print("Would rename {} to {}".format(file_path, new_path))
    else:
        print("Changing {} to {}".format(file_path, new_path))
        os.rename(file_path, new_path)

def replace_string_from_file_name(file_path, string_to_remove, new_string, dry_run=False):
    path, file_name = os.path.split(file_path)
    new_name = file_name.replace(string_to_remove, new_string)
    new_path = os.path.join(path, new_name)
    if dry_run:
        print("Would rename {} to {}".format(file_path, new_path))
    else:
        print("Changing {} to {}".format(file_path, new_path))
        os.rename(file_path, new_path)


def get_file_paths_with_a_string(dir_path, string_to_find):
    return glob.glob(
        os.path.join(dir_path, "*{}*".format(string_to_find))
    )

def setString():
        string_to_remove = '-decrypted'
        global string_choice
        string_choice = input("Press enter to get rid of the default value (-decrypted), or type in your own string to get rid of: ")
        if string_choice == "":
            string_choice = string_to_remove
        print("Your new Target String is: " + string_choice)

def setReplacementString():
        global replacement_string
        replacement_string = input("Enter the value to replace the target value with, or Press enter to go into Remove Mode: ")
        print("Your new Target String is: " + replacement_string)

def menu(firstTime):
    global replacement_string
    if firstTime == True:
        print("\n\nRom Name Cleaner V0.1")
        setString()
    else:
        print("\n\n")
    current_dir = os.getcwd() + "/PutFilesInHere"
    file_paths = get_file_paths_with_a_string(current_dir, string_choice)
    dry_run_choice = input("Options: \n Type 1 for Name Replacement Preview \n 2 for Auto-name Change \n 3 to Change Target String \n 4 to switch to Replacement Mode \n 5 to get rid of Illegal Characters \n Type anything else to close the program \n Enter your choice here: ")
    if dry_run_choice == "1":
        dry_run_choice = True
    elif dry_run_choice == "2":
        dry_run_choice = False
    elif dry_run_choice == "3":
        setString()
        menu(False)
    elif dry_run_choice == "4":
        setReplacementString()
        menu(False)
    elif dry_run_choice == "5":
        illegal_file_paths = get_file_paths_with_a_string(current_dir, "[")
        for file_path in illegal_file_paths:
            replace_string_from_file_name(file_path, "[","(",False)
        illegal_file_paths = get_file_paths_with_a_string(current_dir, "]")
        for file_path in illegal_file_paths:
            replace_string_from_file_name(file_path, "]",")",False)
        menu(False)
    else:
        print("Shutting Down....")
        quit()
    for file_path in file_paths:
        if replacement_string != "":
            replace_string_from_file_name(file_path,string_choice, replacement_string, dry_run=dry_run_choice)
        else:
            remove_string_from_file_name(file_path, string_choice, dry_run=dry_run_choice)
    menu(False)


if __name__ == "__main__":
    global string_choice
    global replacement_string
    string_choice = 'decrypted'
    replacement_string = ""
    menu(True)
