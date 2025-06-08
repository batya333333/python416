from jinja2 import FileSystemLoader,Environment

persons = [
    {"name": "Алексей"},
    {"name": "Никита"},
    {"name": "Виталий"},
]
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('about.html')
msg = tm.render(users=persons, title="About Jinja")

print(msg)