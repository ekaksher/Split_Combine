"""This Tool helps you to split or combine any file. Splitting can be done by two methods.
1. via specifying size of each split file in bytes.
2. via specifying number of parts for splitting.
    byParts must be set to "True" for this method.
    This will inreturn override any size specified by user."""
import os
from math import ceil
def combine(jfile):
    """Combines the splitted parts in one master file.
    Enter the file name with original extension and excluding the .parts extension."""
    if os.path.isfile(jfile+".1"):
        pass
    else:
        print("%s file not found. Please Restart With Correct Path"%jfile)
        return 0
    fcombine = open("combined_"+jfile, "wb")
    try:
        i = 1
        while True:
            if not os.path.isfile(jfile+"."+str(i)):
                print("Operation Completed")
                break
            else:
                filename = jfile+"."+str(i)
                bsize = int(os.stat(filename).st_size)
            print("Writing file... %s to master file."%filename)
            f_read = open(filename, "rb")
            block = 1
            block = f_read.read(bsize)
            fcombine.write(block)
            f_read.close()
            i += 1
    finally:
        fcombine.close()
        print("File Saved Under Name combined_%s in the same directory."%jfile)
def split(file, split_size=1024*1024, by_parts=False, number_of_parts=2):
    """Splits anyfile into any number of parts via desired size and parts option.
    Set by_parts=True to enable splitting by parts.
    Also set any random splitsize as this will be overtaken when by_pparts is set to True."""
    if os.path.isfile(file):
        filesize = os.stat(file).st_size
    else:
        print("%s file not found. Please Restart With Correct Path"%file)
        return 1
    if not by_parts:
        splitsize = int(split_size)
        if splitsize > (int(filesize)):
            print("Split Size Too Large To Split File In Atleast 2 Parts.\n")
            print("Please Re-run With Appropriate Split Size.")
            return 0
        #set a default split size to overcome this.
        parts = int(ceil(int(filesize)/splitsize))
    else:
        parts = number_of_parts
        splitsize = int(ceil((int(filesize))/parts))
    print("Splitting file %s into %s parts"%(file, str(parts)))
    try:
        i = 1
        block = True
        fcombine = open(file, "rb")
        while (block != "" and i <= parts):
            f_write = open(file+"."+str(i), "wb")
            block = fcombine.read(splitsize)
            f_write.write(block)
            f_write.close()
            i += 1
    finally:
        fcombine.close()
    print("Operation Completed.")
    return 0
