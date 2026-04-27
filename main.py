from FinalProject1.logic import *

def main():
    """
    This is the main function that runs the application. It creates an instance 
    of the Logic class, shows the GUI, and starts the event loop.
    """
    app = QApplication([])
    gui = Logic()
    gui.show()
    app.exec()



if __name__ == '__main__':
    main()