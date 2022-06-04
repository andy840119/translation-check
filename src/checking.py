import enum
import json
import logging
import os
import re
import subprocess

logger = logging.getLogger('checking')


class DiffFile:
    file_name = ''
    content = ''


def _list_files_staged_only(extension):
    # list staged files
    output = subprocess.check_output(
        ['git', '--no-pager', 'diff', '--cached', '-z', f'"{extension}"'],
        encoding='utf-8',
    )

    # todo: get content in the file.
    for file in tracked_files:
        logger.debug('file aaa: %r', json.dumps(list(file)))

    return set(
        [
            os.path.normpath(tracked_file)
            for tracked_file in tracked_files
            if re.compile(pattern).match(os.path.basename(tracked_file))
        ]
    )


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
        regex = self._find_tracked_files_extension(Format(format))

        self._tracked_files = _list_files_staged_only(regex)
        logger.debug('Tracked files: %r', self._tracked_files)

        logger.debug('AAA: %r', json.dumps(self._tracked_files))

        # todo: get content in the file.
        for file in self._tracked_files:
            logger.debug('file: %r', json.dumps(list(file)))

        # append .git to exclude folder
        exclude = ['.git']

        # normalize a pathname by collapsing redundant separators
        self._exclude = [os.path.normpath(path) for path in exclude]
        self._mode = CheckMode(mode)

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
