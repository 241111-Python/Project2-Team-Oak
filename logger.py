import controller
from datetime import datetime
import csv

def export(report):
    file = f".\logged_reports\s_report_{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
    with open(file,'w') as f:
        f.write(report)

if __name__ == "__main__":
    r = controller.return_standard_report()
    export(r)