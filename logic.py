from PyQt6.QtWidgets import *
from gui import *
import csv

class Logic(QMainWindow, Ui_Form):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.reset_gui()
        self.submit_button.clicked.connect(lambda: self.submit())
        self.attempt_input.textChanged.connect(lambda: self.show_inputs(self.attempt_input.text()))

    def reset_gui(self) -> None:
        self.hide_inputs()
        
        self.name_input.clear()
        self.attempt_input.clear()
        
        self.score1_input.clear()
        self.score2_input.clear()
        self.score3_input.clear()
        self.score4_input.clear()
        self.score5_input.clear()
        self.score6_input.clear()

        self.file_input.setText("scores.csv")
        self.output_label.setText("")

    def hide_inputs(self) -> None:    
        self.score1_input.hide()
        self.score2_input.hide()
        self.score3_input.hide()
        self.score4_input.hide()
        self.score5_input.hide()
        self.score6_input.hide()
        
        self.score1_label.hide()
        self.score2_label.hide()
        self.score3_label.hide()
        self.score4_label.hide()
        self.score5_label.hide()
        self.score6_label.hide()


    def show_inputs(self, input_attempts) -> None:
        try:
            attempts = int(input_attempts)
            
            if attempts < 1 or attempts > 6:
                self.output_label.setText("Invalid number of attempts")
                return
            if attempts >= 1:
                self.score1_input.show()
                self.score1_label.show()
            if attempts >= 2:
                self.score2_input.show()
                self.score2_label.show()
            if attempts >= 3:
                self.score3_input.show()
                self.score3_label.show()
            if attempts >= 4:
                self.score4_input.show()
                self.score4_label.show()
            if attempts >= 5:
                self.score5_input.show()
                self.score5_label.show()
            if attempts >= 6:
                self.score6_input.show()
                self.score6_label.show()
            self.output_label.setText("")
        
        except (TypeError, ValueError):
            self.output_label.setText("Please enter a valid number of attempts")
            self.hide_inputs()
        
    def write_to_file(self, name, scores) -> None:
        print("began write to file")
        try:
            if self.file_input.text() != None and self.file_input.text().strip() != '':
                with open(self.file_input.text(), 'a+', newline='') as file:
                    writer = csv.writer(file)
                    file.seek(0)
                    
                    if file.read().strip() == '':
                        print('right before header write')
                        writer.writerow(['Name', 'Score 1', 'Score 2', 'Score 3', 'Score 4', 'Score 5', 'Score 6', 'Final'])

                    final_grade = sum(scores) / len(scores)
                    print('right before main write')
                    writer.writerow([name] + scores + [''] * (6 - len(scores)) + [final_grade])
            else:
                self.output_label.setText("Please enter a file name")
        except:
            self.output_label.setText("Error writing to file")

    def submit(self) -> None:
        '''
        This function is called when the submit button is clicked. 
        It validates the input, reorganizes it into two variables,
        calls the write function, and resets the GUI.
        '''

        name = self.name_input.text()
        if name == None or name.strip() == '':
            self.output_label.setText("Please enter a name")
            return
        
        try:
            attempts = int(self.attempt_input.text())
            all_score_input = [self.score1_input.text(), self.score2_input.text(), self.score3_input.text(), self.score4_input.text(), self.score5_input.text(), self.score6_input.text()]
            score_list = []
            for i in range(attempts):
                score_to_append = int(all_score_input[i])
                if 0 <= score_to_append <= 100:
                    score_list.append(score_to_append)
                else:
                    self.output_label.setText("Please enter valid scores (0-100)")
                    return
            
            if '' in score_list:
                self.output_label.setText("Please fill in all score fields")
                return
            
            self.write_to_file(name, score_list)
            
            self.reset_gui()
            self.output_label.setText("Submitted")
        
        except:
            self.output_label.setText("Please enter valid scores (0-100)")
            print("TypeError")
            return
        
