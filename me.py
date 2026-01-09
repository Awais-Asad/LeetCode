import datetime
import subprocess

# Define the bitmap patterns for each letter (7 rows x 5 columns)
letters = {
    'A': [
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1]
    ],
    'W': [
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 0, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1]
    ],
    'I': [
        [1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1]
    ],
    'S': [
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0]
    ]
}

# Sequence for "AWAIS"
sequence = 'AWAIS'

# Collect colored cells (row 1-7, col 1-25)
colored_cells = []
col_start = 1
for char in sequence:
    pattern = letters.get(char, [[0]*5]*7)  # Default empty if not found
    for col_offset in range(5):
        col = col_start + col_offset
        for row in range(1, 8):
            if pattern[row-1][col_offset]:
                colored_cells.append((row, col))
    col_start += 5

# Starting date: June 1, 2025
start_date = datetime.date(2025, 6, 1)

# Compute dates for colored cells
commit_dates = []
for r, c in colored_cells:
    offset = (c - 1) * 7 + (r - 1)
    commit_date = start_date + datetime.timedelta(days=offset)
    commit_dates.append(commit_date)

# Sort dates chronologically
commit_dates.sort()

# Function to run shell commands
def run_cmd(cmd):
    subprocess.check_call(cmd, shell=True)

# Initialize git repository (run this script in an empty directory)
run_cmd('git init')

# Create initial file
with open('contributions.txt', 'w') as f:
    f.write("GitHub contributions art for AWAIS\n")

run_cmd('git add contributions.txt')
run_cmd('git commit -m "Initial commit"')

# Make one commit per selected date
for d in commit_dates:
    strdate = d.isoformat() + 'T12:00:00+0000'  # UTC noon
    with open('contributions.txt', 'a') as f:
        f.write(f"Contribution for {d}\n")
    run_cmd('git add contributions.txt')
    run_cmd(f'GIT_AUTHOR_DATE="{strdate}" GIT_COMMITTER_DATE="{strdate}" git commit -m "Contribution for {d}"')

# After running, add remote and push:
# git remote add origin https://github.com/yourusername/your-repo.git
# git branch -M main
# git push -u origin main
print("Commits created. Now add remote and push to GitHub.")