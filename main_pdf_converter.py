import pdfkit

#Define path to wkhtmltopdf.exe
path_to_wkhtmltopdf = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'

#Define path to HTML file
path_to_file = 'data\\0a1eedc7-0af5-11ee-baf6-4cedfb68e75a.html'

#Point pdfkit configuration to wkhtmltopdf.exe
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

#Convert HTML file to PDF
pdfkit.from_file(path_to_file, output_path='test.pdf', configuration=config, options={"enable-local-file-access": ""})
