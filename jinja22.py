from jinja2 import *


file_loader=FileSystemLoader('templates2')
env = Environment(loader=file_loader)

tm = env.get_template('main.html')
msg = tm.render(title="About Jinja")
print(msg)

