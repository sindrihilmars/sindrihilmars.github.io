import os
import markdown
from bs4 import BeautifulSoup
import argparse

def main():
    # 1. Set up argument parser for command-line usage
    parser = argparse.ArgumentParser(
        description="Converts a Markdown file to HTML and injects it into a target HTML file.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="Example:\n"
               "python update_verkefni2.py Other_Assets/verkefni1.txt Verkefni2.html \"#main .inner\" --clear-selector \"p\""
    )
    parser.add_argument('markdown_file', help='Path to the input Markdown file.')
    parser.add_argument('html_file', help='Path to the target HTML file to modify.')
    parser.add_argument(
        'target_selector',
        help='CSS selector for the element to inject the content into (e.g., "#main .inner").'
    )
    parser.add_argument(
        '--clear-selector',
        dest='clear_selector',
        help='(Optional) CSS selector for elements to remove from the target before injection.\n'
             'Example: "p" to remove all paragraphs.\n'
             'Example: "*" to remove all child elements.'
    )

    args = parser.parse_args()

    # 1. Check if files exist
    if not os.path.exists(args.markdown_file):
        print(f"Error: Could not find {args.markdown_file}")
        return

    if not os.path.exists(args.html_file):
        print(f"Error: Could not find {args.html_file}")
        return

    # 2. Read and Convert Markdown
    print(f"Reading {args.markdown_file}...")
    with open(args.markdown_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    html_content = markdown.markdown(md_content)
    new_soup_content = BeautifulSoup(html_content, 'html.parser')

    # 3. Parse HTML Template
    print(f"Parsing {args.html_file}...")
    with open(args.html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # 4. Locate the target element using the CSS selector
    target_element = soup.select_one(args.target_selector)
    if target_element:
        # If a clear-selector is provided, remove matching elements first
        if args.clear_selector:
            print(f"Clearing elements matching '{args.clear_selector}' from '{args.target_selector}'...")
            for element in target_element.select(args.clear_selector):
                element.decompose()

        # Append the new converted HTML content
        target_element.append(new_soup_content)

        # 5. Save changes
        with open(args.html_file, 'w', encoding='utf-8') as f:
            f.write(str(soup.prettify()))

        print(f"Success! Updated {args.html_file} with content from {args.markdown_file}.")
    else:
        print(f"Error: Could not find the target element with selector '{args.target_selector}' in {args.html_file}.")

if __name__ == "__main__":
    main()