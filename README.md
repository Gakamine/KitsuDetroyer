# What is KitsuDestroyer?
KitsuDestroyer is a list of scripts to clean your Kitsu profile.

# How to use it?
In the root directory of the project, create a ``.env`` file. In the file insert the two following lines:
```
ACCESS_TOKEN=<YOUR TOKEN>
KITSU_ID=<YOUR ID>
```
1. Your Kitsu TOKEN can be found in the localstorage of your browser.
2. You can get your Kitsu ID in your profile picture URL (https://media.kitsu.io/users/avatars/your id>/large.png)

Then, depending of what you want to delete of your profile run, the corresponding script.
For example, you want to delete all your posts: ```python posts.py```