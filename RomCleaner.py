from asyncio.windows_events import NULL
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

def menu(firstTime):
    if firstTime == True:
        print("\n\nRom Name Cleaner V0.1")
        setString()
    else:
        print("\n\n")
    current_dir = os.getcwd()
    file_paths = get_file_paths_with_a_string(current_dir, string_choice)
    dry_run_choice = input("Would you like to preview changes, or make changes: Type 1 for Preview, 2 for Change, 3 to Change Target String, or anything else to close: ")
    if dry_run_choice == "1":
        dry_run_choice = True
    elif dry_run_choice == "2":
        dry_run_choice = False
    elif dry_run_choice == "3":
        setString()
        menu(False)
    else:
        print("Shutting Down....")
        quit()
    for file_path in file_paths:
        remove_string_from_file_name(file_path, string_choice, dry_run=dry_run_choice)
    menu(False)


if __name__ == "__main__":
    global string_choice
    string_choice = 'decrypted'
    menu(True)
