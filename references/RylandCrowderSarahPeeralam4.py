import re
import csv

def get_matching_lines(file_name, input_regex):
    with open(file_name, 'r') as file:
        regex = re.compile(input_regex)
        lines = []
        for l in file.readlines():
            if regex.match(l) != None:
                lines.append(l) 
    return lines

def write_csv(line_list):
    with open('output.csv', 'w', newline='') as file:
        email = ''

        new_text = csv.writer(file)
        new_text.writerow(['Email','Day','Date','Month','Year','Time'])
        for line in line_list:
            temp_list = line.strip().split()
            if temp_list[5][0] == '0':
                temp_list[5] = temp_list[5][1:]
            file.write(f'{temp_list[1]},{temp_list[2]},{temp_list[4]},{temp_list[3]},{temp_list[6]},{temp_list[5]}\n')
            


    print()

def write_txt(line_list):
    count_dict = {}
    with open('output.txt', 'w') as file:
        email = ''
        for line in line_list:
            email = line[6:-1]
            if email in count_dict:
                count_dict[email] += 1
            else: 
                count_dict[email] = 1
        
        file.write(f"{'Email':<40}- Count\n")
        for i in count_dict:
            file.write(f'{i:<40}- {count_dict[i]}\n')
        file.write(f"{'-' * 49}\n")
        file.write(f"{'Total emails':<40}- {len(line_list)}\n")



def main():
    no_colon_regex = r'From .*'
    colon_regex = r'From:.*'
    
    csv_list = get_matching_lines('input.txt', no_colon_regex)
    txt_list = get_matching_lines('input.txt', colon_regex)

    write_csv(csv_list)
    write_txt(txt_list)
    

if __name__ == '__main__':
    main()
