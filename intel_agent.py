import ollama
import re

def security_wrapper(output_text):
    """
    Scans the AI output for sensitive patterns and redacts them.
    """
    deny_list = ["Project-X", "Internal-Only", "Classified-Source"]
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    redacted_text = output_text
    for word in deny_list:
        redacted_text = redacted_text.replace(word, "[REDACTED-KEYWORD]")
    redacted_text = re.sub(email_pattern, "[REDACTED-EMAIL]", redacted_text)
    
    return redacted_text

def generate_intel_brief():
    # Ask the user for the report text.
    print("\n--- PASTE YOUR RAW INTELLIGENCE BELOW (Press Enter + Ctrl-D to finish) ---")
    raw_text = ""
    try:
        while True:
            line = input()
            raw_text += line + "\n"
    except EOFError:
        pass

    if not raw_text.strip():
        print("No text provided. Exiting.")
        return

    # System prompt.
    system_description = (
        "You are a Senior Intelligence Consultant for a risk advisory firm. "
        "Your job is to analyze the provided text and provide a detailed report. "
        "You MUST follow this format exactly. Do not use your own headers. "
        "\n\nFORMAT:\n"
        "1. EXECUTIVE SUMMARY: (BLUF)\n"
        "2. CAPITAL AT RISK: (Financial impact)\n"
        "3. SECURITY IMPLICATIONS: (Physical/Cyber threats)\n"
        "4. FUTURISTIC OUTLOOK: (3-5 year trend prediction)"
    )
    
    print("\n--- ANALYZING LOCALLY... ---\n")

    # The AI call.
    response = ollama.chat(model='llama3', messages=[
        {'role': 'system', 'content': system_description},
        {'role': 'user', 'content': f"Analyze this: {raw_text}"},
    ])
    
    # Apply the security wrapper.
    raw_ai_response = response['message']['content']
    secure_response = security_wrapper(raw_ai_response)

    print("--- SECURE ANALYTICAL BRIEFING ---")
    print(secure_response)

def test_security_wrapper():
    test_cases = [
        ("Information about Project-X is strictly Internal-Only.", "Keywords Check"),
        ("Please contact sarah.doe@startup.ai for the Classified-Source docs.", "Email & Keyword Check"),
        ("This is a clean report with no sensitive data.", "False Positive Check"),
        ("Multiple emails: info@test.com and admin@gov.us", "Multiple Email Check")
    ]

    print("--- STARTING SECURITY VALIDATION ---")
    for text, label in test_cases:
        result = security_wrapper(text)
        print(f"TEST: {label}")
        print(f"INPUT:  {text}")
        print(f"OUTPUT: {result}")
        print("-" * 30)

# Uncomment the line below to run the test.
# test_security_wrapper()

# Run the function.
if __name__ == "__main__":
    generate_intel_brief()