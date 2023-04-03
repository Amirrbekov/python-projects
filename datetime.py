from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, "")

now = datetime.now()

print(datetime.strftime(now, "%Y %B %A"))