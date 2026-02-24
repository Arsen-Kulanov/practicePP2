from datetime import datetime, timedelta

# 1
current_date = datetime.now()
new_date = current_date - timedelta(days=5)

print(new_date)

# 2
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

# 3
now = datetime.now()
without_microseconds = now.replace(microsecond=0)

print(without_microseconds)

# 4
date1 = datetime(2026, 2, 20, 12, 0, 0)
date2 = datetime(2026, 2, 24, 15, 30, 0)

difference = date2 - date1
seconds = difference.total_seconds()

print(seconds)