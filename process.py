#  open the text data file called "um-server-01.txt" to use within this python file
log_file = open("um-server-01.txt")

#  function called sales_reports that takes log_file
#  then loop through log_file to get certain data on column 0 and seeing if the value is "Tue" then print that line.
def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)

#  invoke the function above. 
sales_reports(log_file)
