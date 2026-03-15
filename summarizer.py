import pandas as pd
df = pd.read_csv("parsed_emails.csv")
# Clean subject
df["Subject"] = df["Subject"].astype(str)
# Remove RE and FW
df["Thread"] = df["Subject"].str.replace(r"^(Re:|FW:|Fwd:)\s*", "", regex=True)
# Group emails by thread
threads = df.groupby("Thread")
results = []
for thread, emails in threads:
    # Combine all bodies
    combined_text = " ".join(emails["Body"].astype(str))
    # Key topic = thread name
    key_topic = thread
   # Owner = most frequent sender
    owner = emails["From"].mode()[0]
    # Action items (simple detection)
    action_words = ["schedule", "send", "call", "review", "complete", "update"]
    action_items = []
    for word in action_words:
        if word in combined_text.lower():
            action_items.append(word)

    action_items = ", ".join(action_items) if action_items else "None"

    results.append({
        "Email Thread": thread,
        "Key Topic": key_topic,
        "Action Items": action_items,
        "Owner": owner
    })

result_df = pd.DataFrame(results)

print(result_df)

# Save output
result_df.to_csv("thread_summary.csv", index=False)