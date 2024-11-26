import controller
import os
from datetime import datetime
import csv

def export(report, reportName):
    absPath = os.path.join("logged_reports", f"{reportName}_{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}")
  
    with open(absPath,'w') as f:
        f.write(report)

if __name__ == "__main__":
    r = controller.handle_generate_standard_report()
    export(r)