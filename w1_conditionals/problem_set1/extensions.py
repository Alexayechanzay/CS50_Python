filename = input('File name: ').lower().strip()

if '.gif' in filename:
    a = 'image/gif'
elif '.jpg' in filename or '.jpeg' in filename:
    a = 'image/jpeg'
elif '.png' in filename:
    a = 'image/png'
elif '.jpg' in filename:
    a = 'image/jpeg'
elif '.pdf' in filename:
    a = 'application/pdf'
elif '.txt' in filename:
    a = 'text/plain'
elif '.zip' in filename:
    a = 'application/zip'
else:
    a = 'application/octet-stream'
print(a)