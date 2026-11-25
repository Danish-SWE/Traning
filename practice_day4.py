# the pathlib is used for working with files
# from pathlib import Path
#
# path = Path("test.py")
# path.mkdir()
# print(path.exists())
# print(path.rmdir())

# searching for file/files
# path = Path()
# print(path.glob('*.*')) # means return all files with any format and name
# print(path.glob('*.py')) # all python files in the directory

# show all files inside the directory
# path = Path()
# for file in path.glob('*.*'):
#     print(file)

import openpyxl as xl
from openpyxl.utils import get_column_letter
from pathlib import Path


def calculate_sales_summary(file_path):
    # Support standard excel formats
    valid_extensions = {'.xlsx', '.xlsm', '.xltx', '.xltm'}
    path = Path(file_path)

    if path.suffix.lower() not in valid_extensions:
        raise ValueError(f"Unsupported file format: {path.suffix}. Please convert .xls or .csv to .xlsx first.")

    wb = xl.load_workbook(path)
    # Use active sheet instead of hardcoding 'Sheet1' for better flexibility
    sheet = wb.active

    # 1. Dynamically find where the data starts and ends
    start_row = 3  # Row 1: Title, Row 2: Product Headers
    summary_start_row = None

    for row in range(start_row, sheet.max_row + 1):
        cell_val = str(sheet.cell(row, 1).value or "").strip().lower()
        if "product base total" in cell_val:
            summary_start_row = row
            break

    # Fallback if summary labels aren't pre-written at the bottom
    if summary_start_row is None:
        summary_start_row = sheet.max_row + 1
        sheet.cell(summary_start_row, 1, "Product Base Total")
        sheet.cell(summary_start_row + 1, 1, "Product Base Percentage")
        sheet.cell(summary_start_row + 2, 1, "Grand Total")

    end_data_row = summary_start_row - 1
    total_row = summary_start_row
    pct_row = summary_start_row + 1
    grand_total_row = summary_start_row + 2

    # 2. Calculate Product Base Totals & Grand Total
    grand_total = 0
    product_totals = {}

    # Loop from column 2 (Product A) to the last column
    for col in range(2, sheet.max_column + 1):
        col_sum = 0
        for row in range(start_row, end_data_row + 1):
            val = sheet.cell(row, col).value
            # Safely add only numeric values (ignores blanks or text)
            if isinstance(val, (int, float)):
                col_sum += val

        product_totals[col] = col_sum
        grand_total += col_sum

        # Write Product Base Total
        total_cell = sheet.cell(total_row, col, col_sum)
        total_cell.number_format = '#,##0'

    # 3. Calculate Percentages (Product Total / Grand Total)
    for col, col_sum in product_totals.items():
        pct = (col_sum / grand_total) if grand_total > 0 else 0
        pct_cell = sheet.cell(pct_row, col, pct)
        pct_cell.number_format = '0.00%'

    # 4. Write the Grand Total
    gt_cell = sheet.cell(grand_total_row, 2, grand_total)
    gt_cell.number_format = '#,##0'

    # Save to a new file so original data isn't accidentally overwritten
    output_path = path.with_name(f"{path.stem}_updated{path.suffix}")
    wb.save(output_path)
    print(f"Summary calculated! Saved to: {output_path}")


# Run the function
calculate_sales_summary('store_sales_updated.xlsx')


