from datetime import datetime

# returns date in dd/mm/yyyy format
def get_current_date():
    now = datetime.now()  
    return now.strftime("%d/%m/%Y")
