from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
import os

def create_pdf(user_name, report_year, data, folder="pdfs"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    file_name = f"{user_name}_{report_year}.pdf"
    file_path = os.path.join(folder, file_name)
    document = SimpleDocTemplate(file_path, pagesize=letter)
    content = []

    title = f"{user_name} {report_year}"
    content.append(Table([[title]], colWidths=[460], style=TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, -1), 14),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ])))

    content.append(Table([[""]], colWidths=[460], rowHeights=[20]))

    table_data = [['Имя показателя', 'Значение показателя']]
    table_data.extend(data)

    table_style = TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey)
    ])

    content.append(Table(table_data, colWidths=[230, 230], style=table_style))

    document.build(content)
    return file_path