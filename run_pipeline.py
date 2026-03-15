import subprocess
import sys

print("Starting Email Processing Pipeline...\n")

python = sys.executable  # use the same Python from venv

print("Step 1: Parsing Emails...")
subprocess.run([python, "email_loader.py"])

print("Step 2: Detecting Threads...")
subprocess.run([python, "thread_detector.py"])

print("Step 3: Generating Summaries...")
subprocess.run([python, "summarizer.py"])

print("\nPipeline Completed Successfully!")
print("Dashboard data updated.")