import os.path
import time

paths = str(input(r'Введите путь к файлу: '))
if os.path.isfile(paths):
    a = os.path.getatime(paths)
    print(time.strftime('%d.%m.%Y, %H:%M:%S', time.localtime(a)))
    print(os.path.basename(os.path.dirname(paths)))
    print(os.path.basename(paths))
else:
    a=str(os.path.basename(paths))
    b=str(os.path.basename(os.path.dirname(paths)))
    res=[a,b]
    print(*res)


# Введите путь к файлу: C:\projects\python - topacademy\python hw\homework21fold\h.txt
# 05.04.2025, 22:09:55
# h.txt

# j.txt homework21fold