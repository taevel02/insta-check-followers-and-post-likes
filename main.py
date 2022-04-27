from igramscraper.instagram import Instagram
from time import sleep


followers = []
likes = []

instagram = Instagram()
instagram.with_credentials('plav.official', 'plav8991!')
instagram.login(force=False, two_step_verificator=True)


def get_followers():
    username = 'plav.official'
    account = instagram.get_account(username)
    sleep(1)
    followers_metadata = instagram.get_followers(account.identifier, 1000, 1, delayed=True)

    print('followers count: ', len(followers_metadata['accounts']))

    for follower in followers_metadata['accounts']:
        followers.append(follower.username)


def get_likes():
    media_id = 'CZRCmdHlAsI'
    likes_metadata = instagram.get_media_likes_by_code(media_id, 300)

    print('likes count: ', len(likes_metadata['accounts']))

    for like in likes_metadata['accounts']:
        likes.append(like.username)


if __name__ == '__main__':
    get_followers()
    get_likes()

    # print('follower username: ', followers)
    print('like username: ', likes)

    result = list(set(followers) & set(likes))
    print(result)

    f = open('result.txt', 'w')
    f.write(', '.join(result))
    f.close()
