def summarize_email(email_text):

    words = email_text.split()

    # take first 12 words as summary
    summary = " ".join(words[:12])

    return summary + "..."