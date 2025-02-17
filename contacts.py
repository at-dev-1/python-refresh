contacts = {
    'number': 4,
    'students': [
        {'name': 'Sarah Holderness', 'email': 'Sarah@example.com'},
        {'name': 'John Doe', 'email': 'JohnDoe@example.com'},
        {'name': 'Jane Smith', 'email': 'JaneSmith@example.com'},
        {'name': 'Kyle Brown', 'email': 'KyleBrown@example.com'},
    ]
}

print('Students emails:')
for student in contacts['students']:
    print(student['email'])