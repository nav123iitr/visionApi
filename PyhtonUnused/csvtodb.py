import xlrd
import MySQLdb
book = xlrd.open_workbook('4678_O. P. PHARMA_CORNER STORE TECHNOL.xls')
sheet = book.sheet_by_name('INVOICE')
database = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '', db = 'invoice')
cursor = database.cursor()
query = """INSERT INTO main(bill_no, company, item_name, pack, batch, expiry, mrp) VALUES(%s, %s, %s, %s, %s, %s, %s)"""
for r in range(1, sheet.nrows):
    bill_no = sheet.cell(r, 1).value 
    company = sheet.cell(r, 3).value
    item_name = sheet.cell(r, 6).value
    pack = sheet.cell(r, 7).value
    batch = sheet.cell(r, 8).value
    expiry = sheet.cell(r, 9).value
    mrp = sheet.cell(r, 15).value
    values = (bill_no, company, item_name, pack, batch, expiry, mrp)
    cursor.execute(query, values)

cursor.close()
database.commit()
database.close()    