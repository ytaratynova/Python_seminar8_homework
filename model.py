class_dict = {}
path = ''

def db_path(class_number):
    global path
    path = class_number + ".txt"
    return path


def read_db():
    global class_dict
    pupils_marks_dict = {}
    pmarks_dict = {}

    with open(path, 'r', encoding = 'UTF-8') as file:
        class_info = file.readlines()
        for line in class_info: 
            for pupils_marks in line.split('|')[1].strip().split('; '):
                pupils_marks_dict[pupils_marks.split(':')[0]] = [int(i) for i in pupils_marks.split(':')[1].replace('(','').replace(')','').split(', ')]
            pmarks_dict = {**pmarks_dict,**pupils_marks_dict}
            class_dict[line.split('|')[0]] = pmarks_dict
        # print(class_dict)
        return(class_dict)
    

def get_subject(what_subject):
    global subject
    subject = what_subject
    return subject

def new_mark(pupil, mark) :
    for sub, ppl_marks in class_dict.items():
        if sub == subject:
            journal = class_dict.get(sub)
            for ppl, marks in journal.items():                
                if pupil in ppl:
                    marks.append(mark)
                    

def write_db():
    with open(path, 'w', encoding = 'UTF-8') as file:
        # for i in range(len(class_dict)):
            journal_line = ''
            for sub, ppl_marks in class_dict.items():
                for ppl, marks in class_dict.get(sub).items():
                    journal_line = '; '.join([f"{ppl}: ({', '.join(list(map(str, marks)))})" for ppl, marks in class_dict.get(sub).items()]) + '\n'
                line = ''.join(f'{sub}' +"| " + journal_line)
                file.writelines(line)
        

                  

