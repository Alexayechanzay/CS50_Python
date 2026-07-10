import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r"src=\".*?\"" # non-greedy (lazy) matching 
    match = re.search(pattern, s)
    
    #validate HTML attribute
    if match and "<iframe" in s:
        src, url = match.group().split("=")
        pattern2 = r"https?://(?:www.)?youtube\.com/embed/\w+"

        #validate yt_link
        if yt_link_match := re.search(pattern2, url):

            # extract the yt_link
            yt_link = re.sub(r"https?://(?:www.)?youtube\.com/embed/","", yt_link_match.group())
            return f"https://youtu.be/{yt_link}"
        else:
            return None
    else:
        return None



if __name__ == "__main__":
    main()