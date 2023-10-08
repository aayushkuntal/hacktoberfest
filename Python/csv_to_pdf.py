import csv
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Define the CSV file input and PDF file output
csv_file = 'input.csv'
pdf_file = 'output.pdf'

# Read the CSV file and store its data in a list
data = []
with open(csv_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        data.append(row)

# Create a PDF document
pdf = SimpleDocTemplate(pdf_file, pagesize=letter)

# Create a table from the CSV data
table = Table(data)

# Style the table
style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), (0.8, 0.8, 0.8)),  # Header row background color
    ('TEXTCOLOR', (0, 0), (-1, 0), (0, 0, 0)),  # Header row text color
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center alignment for all cells
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header font
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Bottom padding for header row
    ('BACKGROUND', (0, 1), (-1, -1), (0.95, 0.95, 0.95)),  # Data row background color
    ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),  # Table grid
])

table.setStyle(style)

# Build the PDF document
elements = [table]
pdf.build(elements)

print(f'PDF file "{pdf_file}" has been generated.')
