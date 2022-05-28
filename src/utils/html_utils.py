import re


def get_content_in_the_html(html):
    # see: https://stackoverflow.com/a/59446438/4105113
    spacing_regex = '\s*'
    html_regex = f'(?<=>){spacing_regex}([\w\s]+){spacing_regex}(?=<\/)'
    result = re.findall(html_regex, html)
    return [i for i in result if i and not i.isspace()]
