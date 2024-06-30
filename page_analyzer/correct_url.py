from urllib.parse import urlparse
import validators


def correct_url(url):
    parsed_url = urlparse(url)

    if all([parsed_url.scheme, parsed_url.netloc]) and len(url) > 255:
        return 'URL превышает 255 символов'
    if validators.url is not True:
        return 'Некорректный URL'
