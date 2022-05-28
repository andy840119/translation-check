import pytest

from src.utils.html_utils import get_content_in_the_html


@pytest.mark.parametrize('test_html, expected', [
    ('<div>Content</div>', ['Content']),
    ('<br>Content</br>', ['Content']),  # should be works in another type of html tag.
    ('<div><br>Content</br></div>', ['Content']),  # should not get the tag.
    ('<div class="fa fa-home">Content</div>', ['Content']),
    # should be able to get the content if has property in the html.
    ('<div>  </div>', []),  # should ignore spacing.
    ('<div> Content</div>', ['Content']),  # ignore spacing
])
def test_get_content_in_the_html(test_html, expected):
    actual = get_content_in_the_html(test_html)
    assert expected == actual


# remain
@pytest.mark.skip(reason='Waiting for implementation.')
@pytest.mark.parametrize('test_html, expected', [
    ('<div>Content1<br>Content2</br>Content3</div>', ['Content1', 'Content2', 'Content3']),  # should not get the tag.
    ('<div>Content </div>', ['Content']),  # ignore spacing
])
def test_get_content_in_the_html_todo(test_html, expected):
    actual = get_content_in_the_html(test_html)
    assert expected == actual
