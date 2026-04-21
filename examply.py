def get_scores():
    #get inputs
    how_many = input('Total number of students: ')
    while how_many.isdigit() == False:
        how_many = input('Please enter a number: ')
    how_many = int(how_many)

    scores = input(f'Enter {how_many} score(s): ').split()
    #check to make sure all scores are ints and there are enough scores
    are_scores_digits = [False for i in scores if i.isdigit() == False]
    while len(scores) < how_many or False in are_scores_digits: # added .isdigit, don't know if it will work
        scores = input(f'Enter {how_many} score(s): ').split()
        are_scores_digits = [False for i in scores if i.isdigit() == False]
    
    scores = [int(i) for i in scores]
    return scores[0:how_many]

def print_grades(scores_list):
    best_score = max(scores_list)
    for i in range(len(scores_list)):
        print(f'Student {i+1} score is {scores_list[i]} and grade is {calculate_grade(scores_list[i], best_score)}')
    avg_score = sum(scores_list) / len(scores_list)
    print(f'The average score is {avg_score:.2f}, a grade of {calculate_grade(avg_score, best_score)}')
          
def calculate_grade(inp_grade, best_score=100):
    grade = 0
    if inp_grade >= best_score - 10:
        return 'A'
    elif inp_grade >= best_score - 20:
        return'B'
    elif inp_grade >= best_score - 30:
        return 'C'
    elif inp_grade >= best_score - 40:
        return 'D'
    else:
       return 'F'

if __name__ == '__main__':
    print_grades(get_scores())