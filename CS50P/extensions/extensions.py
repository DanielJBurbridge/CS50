import re
extension = input("file exension: ").strip().lower()

media_type_key = [
    ('.*\.gif$', 'image/gif'),
    ('.*\.jpg$', 'image/jpeg'),
    ('.*\.jpeg$', 'image/jpeg'),
    ('.*\.png$', 'image/png'),
    ('.*\.pdf$', 'application/pdf'),
    ('.*\.txt$', 'text/plain'),
    ('.*\.zip$', 'application/zip')
]

matches = []
for key, value in media_type_key:
    matches.append(bool(re.match(key, extension)))
    extension = re.sub(key, value, extension)

if True in matches:
    pass
else:
    extension = 'application/octet-stream'


print(extension)