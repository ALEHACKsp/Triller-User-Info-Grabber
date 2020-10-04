# Triller User Info Grabber
Returns Triller users' exact locations, date of birth, mobile operating systems and more.

## Information
So, I was bored and monitored a few requests in the official Triller mobile application. I found some interesting data that should not be returned in plain text or even returned at all. If you report a comment on a Triller video, it returns the EXACT location (in latitude and longitude) of where the comment was posted from, the user's date of birth, operating system, gender and more. I made a simple script filtering verified users and a few celebrities of my choice. However, it looks like it has been patched and that they are aware of this issue, because it only works on old comments.

There are other ways of fetching this data — without having to spam report; but I found them after this one. I am still surprised how people think Triller is more secure than TikTok; your data is not safe with them.

Please refrain from using this tool as it is spamming Triller's API. I posted this to demonstrate how your information can easily be leaked. You should not trust every application.

I used a static auth_token and one proxy to make it easier for them to clean up the mess. I am hoping for this to get patched, but meanwhile, using this will be under your own responsibility.

## Preview
![](https://i.imgur.com/mXKIj4n.png)<br>
![](https://i.imgur.com/LxnrXMu.jpg)<br>
![](https://i.imgur.com/ae1WOAQ.png)

## Usage
- Python 3.8 or above is required.
- I develop for Windows machines only and do not intentionally support other operating systems.

Run the following command to install the required dependencies; make sure PIP is added to PATH.
```
pip3 install requests==2.24.0
```
1. Edit the targeted celebrities in the "variables" instance attribute if you want to. I could not be bothered making it more user-friendly — I was not planning on releasing it.
2. Run main.py
3. All set!

## Legal Notice
This is illegal if you use it without the consent of the creators — in this case, the Triller team. I am not accountable for any of your actions; this was merely a speedrun to demonstrate how your data can easily be leaked and filtered. Please do not misuse this tool.
