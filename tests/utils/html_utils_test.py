import pytest

from src.utils.html_utils import (
    get_angular_template_content_from_html_content, get_content_in_the_html,
    get_fms_template_content_from_html_content)


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


@pytest.mark.parametrize('test_content, expected', [
    ('{{_T.TEXT}}', ['_T.TEXT']),
    ('  {{_T.TEXT}}', ['_T.TEXT']),  # should ignore the spacing.
    ('{{_T.TEXT}}  ', ['_T.TEXT']),  # should ignore the spacing.
    ('{{call()}}', ['call()']),
    ('{{getStartTime()}} ~ {{getEndTime()}}', ['getStartTime()', 'getEndTime()']),
])
def test_get_angular_template_content_from_html_content(test_content, expected):
    actual = get_angular_template_content_from_html_content(test_content)
    assert expected == actual


@pytest.mark.skip(reason='Waiting for implementation.')
@pytest.mark.parametrize('test_content, expected', [
    ('{{ _T.TEXT }}', ['_T.TEXT']),  # should ignore the spacing in the internal.
])
def test_get_angular_template_content_from_html_content_todo(test_content, expected):
    actual = get_angular_template_content_from_html_content(test_content)
    assert expected == actual


@pytest.mark.parametrize('test_content, expected', [
    ('[[_T.TEXT]]', ['_T.TEXT']),
    ('  [[_T.TEXT]]', ['_T.TEXT']),  # should ignore the spacing.
    ('[[_T.TEXT]]  ', ['_T.TEXT']),  # should ignore the spacing.
    ('[[call()]]', ['call()']),
    ('[[getStartTime()]] ~ [[getEndTime()]]', ['getStartTime()', 'getEndTime()']),
])
def test_get_fms_template_content_from_html_content(test_content, expected):
    actual = get_fms_template_content_from_html_content(test_content)
    assert expected == actual


@pytest.mark.skip(reason='Waiting for implementation.')
@pytest.mark.parametrize('test_content, expected', [
    ('[[ _T.TEXT ]]', ['_T.TEXT']),  # should ignore the spacing in the internal.
])
def test_get_fms_template_content_from_html_content_todo(test_content, expected):
    actual = get_fms_template_content_from_html_content(test_content)
    assert expected == actual
