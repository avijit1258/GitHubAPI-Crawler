import csv
import sys

file_name = ''

def reading_a_text_file(filename):
    ''' This function reads a text file and outputs list of lines where line contents are
        seperated by commas
    '''

    cross_reference_issue_file = open(filename, 'r')

    issues = cross_reference_issue_file.readlines()

    list_of_lines = []
    count = 0
    for line in issues:
        if '403' in line:
            continue
        else:
            count = count + 1
            contents = line.strip().split(',')
            list_of_lines.append([count] + contents)

    return list_of_lines

def list_of_lines_to_csv(list_of_lines):
    with open( file_name[0 : file_name.find('.')] +'.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['ID', 'Src Issue', 'Type', 'Ref Issue/PR', 'Type'])
        for i in list_of_lines:
            csvwriter.writerow(i)

    return 

if __name__ == "__main__":
    file_name = str(sys.argv[1])
    list_of_lines_to_csv(reading_a_text_file(file_name))




    