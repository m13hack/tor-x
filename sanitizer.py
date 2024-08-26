import re
import argparse

def sanitize(text):
    sanitized_text = re.sub(r'\b(?:http|https):\/\/\S+\b', '[REDACTED]', text)
    return sanitized_text

def main():
    parser = argparse.ArgumentParser(description='Sanitize sensitive information from text.')
    parser.add_argument('--text', required=True, help='Text to sanitize')
    args = parser.parse_args()

    sanitized = sanitize(args.text)
    print(sanitized)

if __name__ == '__main__':
    main()
