import os


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    return (len(os.walk(path).next()[1]), len(os.walk(path).next()[2]))

