import pandas as pd
import re

# Load parsed emails
df = pd.read_csv("parsed_emails.csv")

# Function to clean subject
def clean_subject(subject):
    subject = str(subject)
    subject = re.sub(r"^(Re:|FW:|Fwd:)\s*", "", subject, flags=re.IGNORECASE)
    return subject.strip()

# Create thread column
df["Thread"] = df["Subject"].apply(clean_subject)

# Group by thread
threads = df.groupby("Thread")

# Print thread summary
for thread, emails in threads:
    print("\n====================")
    print("THREAD:", thread)
    print("Total Emails:", len(emails))