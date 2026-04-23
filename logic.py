from PyQt6.QtWidgets import *
from gui import *
import csv

class Logic(QMainWindow, Ui_Form):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.reset_gui()
        self.submit_button.clicked.connect(lambda: self.submit)
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
        self.score5_label.hide()
        self.score6_label.hide()
        self.score3_label.hide()
        self.score4_label.hide()


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
        
    def write_to_file(self, name, scores):
        try:
            with open('scores.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                final_grade = max(scores) # figure this out
                writer.writerow([name] + scores + [''] * (6 - len(scores)) + [final_grade])
        except:
            self.output_label.setText("Error writing to file")

    def submit(self):
        name = self.name_input.text()
        if name == "":
            self.output_label.setText("Please enter a name")
            return
        
        try:
            attempts = int(self.attempt_input.text())
            score_list = []
            for i in range(attempts):
                score_list.append(exec(f'self.score{i+1}_input.text()'))
            
            if '' in score_list:
                self.output_label.setText("Please fill in all score fields")
                return
            
            self.write_to_file(name, score_list)
        except (TypeError, ValueError):
            self.output_label.setText("Error writing to file")
            return
        
