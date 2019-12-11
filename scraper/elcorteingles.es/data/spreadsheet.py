import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
# from scrapers.elcorteingles.spiders.data.get_data import items

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

worksheet = client.open("test").sheet1  # Open the spreadhseet

data = worksheet.get_all_records()  # Get a list of all records
print(data)




# row = sheet.row_values(3)  # Get a specific row
# col = sheet.col_values(3)  # Get a specific column
# cell = sheet.cell(1,2).value  # Get the value of a specific cell

# my_row = ["hello", 1, "red", "blue"]
# sheet.add_rows(5)  # Insert the list as a row at index 4
# valor = sheet.row_values(5)
# sheet.update_cell(2,2, "CHANGED")  # Update one cell
# sheet.update_acell('B1', 'Bingo!')

# numRows = sheet.row_count  # Get the number of rows in the sheet

def save(items): 
    
    for row, title in enumerate(items['title'], start=1):
        if not 'favoritos' in title:
            worksheet.update_cell(row, 4, title)
        
    for row, precio in enumerate(items['precio'], start=1):     
        worksheet.update_cell(row, 5, precio)



