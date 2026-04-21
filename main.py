from logic import *

def main():
    app = QApplication([])
    gui = Logic()
    gui.show()
    app.exec()



if __name__ == '__main__':
    main()