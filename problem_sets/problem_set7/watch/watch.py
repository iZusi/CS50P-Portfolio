import re

def parse(html):
    # define the regex pattern for the url
    url_pattern = r"https?://(?:www\.)?youtube\.com/embed/(\w+)"

    # use re.search to find the first matching url in the HTML
    match = re.search(url_pattern, html, re.IGNORECASE)

    if match:
        # extract the video ID from the matched url
        video_id = match.group(1)

        # Generate the youtu.be url
        url = f"https://youtu.be/{video_id}"

        return url

def main():
    # get user input (HTML snippet)
    html = input("HTML: ").strip()

    if html.startswith("https://"):
        return None
    else:
        # call the parse function for extraction and print output
        result = parse(html)
        print(result)

if __name__ == "__main__":
    main()
