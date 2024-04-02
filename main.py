# Part 1
def read_csv(filename):
   """
    Open and read the file 
    convert year and enrolment to int 
    """
   filename = 'pre-u-enrolment-by-age.csv'
   header = []
   data = []
   with open(filename, 'r') as f:
       header = f.readline().strip().split(',')
       
       for line in f:
           line_data = line.strip().split(',')
           int_line = [int(line_data[0]), int(line_data[3])]
           data.append(int_line)
           
           return (header, data)

                   




# Part 2
def filter_gender(enrolment_by_age, sex):
    # Type your code below

    '''
    removes the gender from data
    '''  

    with open('pre-u-enrolment-by-age.csv', 'w') as f:
        data1 = []
        for data in enrolment_by_age:
            if data[2] == sex:
                data1 = [data[0], data[1], data[3]]
                data1.append([data])

                return data1






# Part 3
def sum_by_year(enrolment):
    # Type your code below
    '''
    returns enrolment year 
    '''
    with open('pre-u-enrolment-by-age.csv', 'w') as f:
        data2 = []
        enrolment_by_year = []
        for data in enrolment:
            if enrolment == data[2]:
                enrolment_by_year = [data[0], data[2]]
                data2 = [enrolment_by_year]

                return data2





# Part 4
def write_csv(filename, header, data):
    # Type your code below
    with open('pre-u-enrolment-by-age.csv', 'w') as f:
        header = []
        data = []

        filename = 'total-enrolment-by-year.csv'
        header = f.readline().strip().split(',')
 


# TESTING
# You can write code below to call the above functions
# and test the output
