import model
import view


model.db_path(view.input_class())
model.read_db()

def start():
    match view.class_menu():
        case 1:
            subject = model.get_subject(view.input_subject())
            view.subject_journal(model.class_dict, subject)
            while True:
                match view.teacher_menu():
                        case 1:
                            model.new_mark(view.pupil_name(), view.what_mark())
                            model.write_db()
                            view.subject_journal(model.class_dict, subject)
                        case 2:
                            start()
        case 2:
            view.pupil_marks(model.class_dict,view.pupil_name())
            start()
        case 3:
              view.exit_program()
              
            



