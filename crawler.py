from requester import Requester
from common import config_reader, config_intervaltime
import post
import time
import rediscache


class TiebaCrawler(Requester):
    """ Post crawler  , gather information of posts in given bar
        can't get image submmited in post
    """

    def __init__(self, tieba_name="steam", cookie=None):
        """
        :param tieba_name:
        :param cookie:
        """
        Requester.__init__(self, tieba_name, cookie)

    def __avaiable_check(self):
        # response = self.session_worker
        pass

    def get_posts(self):
        """
        Get all posts on first page of tieba , and generate a post objects list
        :return list of Post object:
        """
        soup = self.get_content(self.tieba_base)

        post_a = self.__get_posts_a(soup)

        url_list = [self.url_base + tag.get('href') for tag in post_a]

        post_dict = self.__get_content_list(url_list)
        post_list = [post.Post(url, soup) for url, soup in post_dict.items()]

        return post_list

    @rediscache.postcache
    def __get_content_list(self, url_list):
        """
        Get post content with given url list
        :param url_list:
        :return dict:
        """
        content_list = {}

        for url in url_list:
            content = self.get_content(url)
            if content:
                content_list[url] = content

            time.sleep(config_intervaltime())

        return content_list

    def __get_posts_a(self, soup):
        """
        Get all post url from the soup of first page of tieba
        :param soup:
        :return list of posts' url:
        """
        posts_list = soup.findAll('div', {'class': 'i'})
        posts_list = [tag.find('a') for tag in posts_list if not tag.find('span', {'class': 'light'})]
        return posts_list


if __name__ == "__main__":
    cookie, _ = config_reader()
    tieba_worker = TiebaCrawler(cookie=cookie, tieba_name='dota2提问')
    posts = tieba_worker.get_posts()
    print(len(list(map(str, posts))))
    posts = tieba_worker.get_posts()
    print(len(list(map(str, posts))))
    # print(list(map(str, posts[0].reply_list)))
