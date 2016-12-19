![](/meta/iShovel.png)

> **iShovel** is a disruptive language picker for teams in a hurry. It suggests you a language on the basis of the languages you have worked on in past along with the latest technologies which you (or any of your team members) haven't ever used.

## How iShovel Works
You enter the usernames of your team members and iShovel digs the GitHub APIs and extracts the amount of work you have donw for each language.

It also intelligently incorporates the fact that different people would have varied contributions but equal knowledge / experience with the language.

After digging is complete, **iShovel suggests you some language along with a percentage score with which it thinks you should go ahead with**.


## Setup
```bash
git clone https://github.com/prabhakar267/iShovel.git && cd iShovel
```
```bash
pip install virtualenv
virtualenv venv
source venv/bin/activate
```
```
[sudo] pip install -r requirements.txt
```
+ Edit [project.cfg.sample](project.cfg.sample) and add your GitHub username and password for seamless digging of data from GitHub servers.
```
python main.py
```

## Inspiration

We ([prabhakar267](https://github.com/prabhakar267) and [mbad0la](https://github.com/mbad0la)) were sitting in a hackathon and were sure of an idea which we wanted to implement but not sure of the language with which we should develop it. We had experience with PHP, Python and JavaScript but didn't want to go ahead with one of these so we built a script first which suggests us a language. 
Eventaully we ended up building our hackathon project in **Ruby**.
