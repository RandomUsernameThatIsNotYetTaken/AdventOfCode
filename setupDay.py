import sys
import datetime
import os
import subprocess
import sys
import subprocess


#takes year and day as an input or defaults to current year and day
year = sys.argv[1] if len(sys.argv) > 1 else "2023"
day = sys.argv[2] if len(sys.argv) > 2 else datetime.datetime.now().day
day = str(day).zfill(2)


# Check Python version
if sys.version_info < (3, 9):
  print("Python version 3.9 or higher is required.")
  sys.exit(1)

  try:
    subprocess.run("advent-of-code-data --version", shell=True, check=True)
    print("advent-of-code-data is installed.")
  except subprocess.CalledProcessError:
    print("advent-of-code-data is not installed.")
    print("Run the following with pip.9 or higher:")
    print("pip install advent_of_code_data.whl")
    



year = sys.argv[1] if len(sys.argv) > 1 else "2023"
day = sys.argv[2] if len(sys.argv) > 2 else datetime.datetime.now().day
day = str(day).zfill(2)

# Rest of your code...

year_folder = f"/home/kobe/gitrepositories/personal/AdventOfCode/{year}"
if not os.path.exists(year_folder):
  os.makedirs(year_folder)
day_folder = f"{year_folder}/{day}"
if not os.path.exists(day_folder):
  os.makedirs(day_folder)
subprocess.run(f"cd {day_folder} && touch {year}_{day}.input", shell=True)
subprocess.run(f"cd {day_folder} && aocd {year} {day} > {year}_{day}.input", shell=True)
subprocess.run(f"cd {day_folder} && aocd {year} {day}  --example >{year}_{day}_sample.input", shell=True)
subprocess.run(f"cd {day_folder} && echo 'with open(\"{year}_{day}.input\", \"r\") as f:' >> day{day}_part1.py", shell=True)
subprocess.run(f"cd {day_folder} && chmod +x day{day}_part1.py", shell=True)

# Open the sample input file and strip lines that contain "--------"
with open(f"{day_folder}/{year}_{day}_sample.input", "r") as f:
  sample_input = f.read().split('--------------------------------------------------------------------------------')
  sample_input = sample_input[0]
  sample_input = sample_input.split('\n')
  sample_input = sample_input[3:]
  print(sample_input)

# Write sample_input to the sample.input file
with open(f"{day_folder}/{year}_{day}_sample.input", "w") as f:
  f.write('\n'.join(sample_input))
  
# Rest of your code...

