import markdown
import zipfile
import os
def generate_html_from_md(data):
    """
    Generate html from markdown
    """
    return markdown.markdown(data)

def create_html_file(filename,html_code):
    path = os.path.join(os.getcwd(),'tmp')
    filepath = os.path.join(path,os.path.splitext(filename)[0] + '.html')
    with open(filepath,'w') as f:
        f.write(html_code)
    return filepath

def create_zip(sitename,files):
    path = 'tmp'
    filename = f'{sitename}.zip'
    filepath = os.path.join(path,filename)
    print(filepath)
    
    with zipfile.ZipFile(filepath,'w') as zip:
        for file in files:
            segments= os.path.split(file)
            zip.write(file,segments[1])
    return filepath