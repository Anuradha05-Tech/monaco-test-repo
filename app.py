import subprocess

def run_backup(filename):
    # BUG: shell=True + unsanitized input = command injection
    subprocess.run(f"tar -cvf backup.tar {filename}", shell=True)

API_KEY = "sk-hardcoded-secret-12345"  # BUG: hardcoded secret
SECRET_TOKEN = 'sk-another-test-secret-999'  # another hardcoded secret
SECRET_TOKEN = 'sk-another-test-secret-999'  # another hardcoded secret
