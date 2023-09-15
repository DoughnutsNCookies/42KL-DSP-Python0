from datetime import datetime

current_time = datetime.now().timestamp()
print("Seconds since January 1, 1970:",
      "{:,.4f}".format(current_time), "or",
      "{:.2e}".format(current_time), "in scientific notation")

# Print in MON DD YYYY
print(datetime.now().strftime("%b %d %Y"))
