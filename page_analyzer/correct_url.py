from urllib.parse import urlparse
import validators


# def normalize_url(url):
#     normal_url = urlparse(url)
#     return normal_url
#
#
# def validator_url(url):
#     valid_url = validators.url(url)
#     return valid_url


def correct_url(url):
    parsed_url = urlparse(url)

    if len(url) > 255:
        return 'URL превышает 255 символов'
    if urlparse(url) is not True:
        return 'Некорректный URL'

    pass
