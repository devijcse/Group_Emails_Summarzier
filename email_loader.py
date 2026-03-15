import pandas as pd
import re

# Load dataset
df = pd.read_csv("DataSet/emails.csv")

emails = df["message"].head(10)

parsed_emails = []

for email in emails:

    # Extract subject
    subject = re.search(r"Subject: (.*)", email)
    subject = subject.group(1) if subject else "No Subject"

    # Extract sender
    sender = re.search(r"From: (.*)", email)
    sender = sender.group(1) if sender else "Unknown"

    # Extract body (text after X-FileName)
    body_split = email.split("X-FileName:")
    body = body_split[1] if len(body_split) > 1 else ""

    parsed_emails.append({
        "Subject": subject,
        "From": sender,
        "Body": body.strip()
    })

# Convert to DataFrame
parsed_df = pd.DataFrame(parsed_emails)

print(parsed_df)
parsed_df.to_csv("parsed_emails.csv", index=False)