import os
import sys

commit_command = 'git commit -m "Update files"'
force = False

# Check the command line arguments for a custom commit message
if len(sys.argv) == 3 and sys.argv[1] == '-m':
    commit_command = f'git commit -m "{sys.argv[2]}"'

print('add-commit-push')
print('\ngit status')
os.system('git status')

# Check for the '-f' option
for x in range(len(sys.argv)):
    if sys.argv[x] == '-f':
        force = True

print(force)

# Prompt the user for confirmation
if not force:
    print("Continue with add, commit, push? (y):")
    userInput = input()
    if userInput.lower() != 'y':
        print('Canceling program')
        quit()

# Execute Git commands with error handling
try:
    print('\ngit add -A')
    os.system('git add -A')
    print(f'\n{commit_command}')
    os.system(commit_command)
    print('\ngit push')
    os.system('git push')
except Exception as e:
    print(f'An error occurred: {str(e)}')
