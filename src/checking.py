import enum
import json
import logging
import subprocess

logger = logging.getLogger('checking')


class DiffFile:
    file_name = ''
    content = ''


def _list_files_staged_only(extension):
    logger.debug('Row lines: %r', ['git', '--no-pager', 'diff', '--cached', '-z', f'{extension}'])

    # list staged files
    # git --no-pager diff --cached -z "*.component.html"
    output = subprocess.check_output(
        ['git', '--no-pager', 'diff', '--cached', '-z', f'{extension}'],
        encoding='utf-8',
    ).split('\n')

    logger.debug('Row lines: %r', output)

    files = []

    for line in output:
        # ignore the line like:
        # diff --git a/container-date-filter.component.html b/container-date-filter.component.html
        # index 5cb09e4ea9..e1e175b654 100644
        if line.startswith('diff') or line.startswith('index'):
            continue

        # ignore the line like:
        # @@ -73,4 +73,4 @@
        if line.startswith('@@'):
            continue

        if line.startswith('+++ '):
            new_diff_file = DiffFile()
            # todo: might cause remove the path if contains matched string, but it's OK for now.
            new_diff_file.file_name = line.replace('+++ ', '')
            files.append(new_diff_file)

        # should not process if there's no files created.
        if len(files) == 0:
            continue

        if line.startswith('+'):
            files[-1].content += f'\n{ line[1:] }'

        if line.startswith('-'):
            continue

        files[-1].content += f'\n{line}'

    return files


class Format(enum.Enum):
    HTML = 'html'
    ANGULAR = 'angular'
    PYTHON = 'python'

    def __str__(self):
        return self.value


class CheckMode(enum.Enum):
    CHECK_MISSING_TRANSLATE = 'check_missing_translate'
    GET_ALL_TRANSLATE_FILE_PATH = 'get_all_translate_file_paths'

    def __str__(self):
        return self.value


class Checking:
    def __init__(self, format, mode):
        extension = self._find_tracked_files_extension(Format(format))

        self._tracked_files = _list_files_staged_only(extension)
        self._mode = CheckMode(mode)

        logger.debug('Tracked files: %r', self._tracked_files)

        # todo: get content in the file.
        for file in self._tracked_files:
            logger.debug('file: %r', json.dumps(file))

    @staticmethod
    def _find_tracked_files_extension(format):
        if format == Format.HTML:
            return '*.html'
        elif format == Format.ANGULAR:
            return '*.component.html'
        elif format == Format.PYTHON:
            return '*.py'
        else:
            raise Exception()

    def run(self) -> int:
        fail = 0

        # todo: waiting for implementing.
        # if self._find_for_unittest():
        #     fail = 1
        logger.debug('Tracked files: %r', self._tracked_files)

        return fail
