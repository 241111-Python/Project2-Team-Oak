import controller
import os
from datetime import datetime
import csv

def export(report):
    file = f"C:\Revature\Project2-Team-Oak\logged_reports\s_report_{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
    absPath = os.path.abspath(file)
    with open(absPath,'w') as f:
        f.write(report)

if __name__ == "__main__":
    r = controller.handle_generate_standard_report()
    export(r)