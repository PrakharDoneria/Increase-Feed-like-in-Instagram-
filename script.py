from instapy import InstaPy


insta_username = 'PrakharDoneria'
insta_password = 'MyPàssw0RD'


session = Instapy(username=insta_username, password=insta_password)
session.login()

session.like_by_feed(amount=100, randomize=True, unfollow=True, interact=True)
