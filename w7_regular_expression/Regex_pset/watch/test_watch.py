import re
s = input("HTML: ")
#<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>

pattern = r"src=\".*?\"" # non-greedy matching (lazy)
match = re.search(pattern, s)
if match and  "<iframe" in s:
    src, url = match.group().split("=")
    pattern2 = r"https?://(?:www.)?youtube\.com/embed/\w+"

    if yt_link_match := re.search(pattern2, url):
        # valid yt_link
        print(yt_link_match)

        # extract the yt_link
        yt_link = re.sub(r"https?://(?:www.)?youtube\.com/embed/","", yt_link_match.group())
        print(yt_link)
        #print(f"https://youtu.be/{yt_link}")
    else:
        print("Invalid youtube link: None")
else:
    print("Not match")