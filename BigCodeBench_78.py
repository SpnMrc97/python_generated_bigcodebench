import csv
import io
from django.http import HttpRequest, FileResponse

def task_func(request, header, csv_data):

    # Create a StringIO object to write CSV data
    csv_buffer = io.StringIO()
    
    # Create a CSV writer object
    csv_writer = csv.writer(csv_buffer)
    
    # Write the header to the CSV
    csv_writer.writerow(header)
    
    # Write the data rows to the CSV
    csv_writer.writerows(csv_data)
    
    # Move to the beginning of the StringIO buffer
    csv_buffer.seek(0)
    
    # Create a FileResponse object to return as a response
    response = FileResponse(csv_buffer, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    
    return response
