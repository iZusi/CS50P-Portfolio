# Prompt the user for a file name and convert it to lowercase with leading/trailing whitespace removed
file_name = input('File name: ').lower().strip()

# Check if the file name contains the extension '.jpg' or '.jpeg'
if '.jpg' in file_name or '.jpeg' in file_name:
    # If either extension is found, print 'image/jpeg'
    print('image/jpeg')
# Check if the file name contains the extension '.gif'
elif '.gif' in file_name:
    # If the extension is found, print 'image/gif'
    print('image/gif')
# Check if the file name contains the extension '.png'
elif '.png' in file_name:
    # If the extension is found, print 'image/png'
    print('image/png')
# Check if the file name contains the extension '.pdf'
elif '.pdf' in file_name:
    # If the extension is found, print 'application/pdf'
    print('application/pdf')
# Check if the file name contains the extension '.txt'
elif '.txt' in file_name:
    # If the extension is found, print 'text/plain'
    print('text/plain')
# Check if the file name contains the extension '.zip'
elif '.zip' in file_name:
    # If the extension is found, print 'application/zip'
    print('application/zip')
# If none of the above conditions are met, assume a generic binary file and print 'application/octet-stream'
else:
    print('application/octet-stream')
