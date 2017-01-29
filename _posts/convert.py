"""Converts .html posts that have been converted by the jekyll-import tool to
Makrdown format."""

import os
import sys
import re


def read_file(file_name):
    return open(file_name).read()


def write_file(file_name, content):
    with open(file_name, 'w') as f:
        f.write(content)


def replace_html_tags(text):
    text = re.sub(r'<p>', '', text)
    text = re.sub(r'</p>', '\n', text)
    text = re.sub(r'<br />', '', text)

    return text


def insert_redirect_from_predicate(text):
    s = re.search(r"post_id: '(\d+)'", text)
    post_id = s.group(1)

    index = text.find('\n---\n', 3)

    prefix = text[:index]
    suffix = text[index:]

    predicate = '''
redirect_from:
  - /archives/{}/'''.format(post_id)

    return prefix + predicate + suffix


def insert_redirect_to_predicate(text, filename):
    index = text.find('\n---\n', 3)

    prefix = text[:index]
    suffix = text[index:]

    slug = basename_without_extension(filename)[11:]

    predicate = '''
redirect_to:
  - http://philosophical.one/post/{}'''.format(slug)

    return prefix + predicate + suffix



def insert_absolute_url(text):
    return text.replace(
        'src="/wp-content',
        'src="http://blog.suminb.com/wp-content')


def basename_without_extension(full_path):
    basename = os.path.basename(full_path)
    return os.path.extsep.join(os.path.splitext(basename)[:-1])


def migrate1():
    source_file_name = sys.argv[1]
    source_file_name_noext = os.path.splitext(source_file_name)[0]
    target_file_name = '{}.markdown'.format(source_file_name_noext)

    content = read_file(source_file_name)
    content = replace_html_tags(content)
    content = insert_redirect_from_predicate(content)
    content = insert_absolute_url(content)

    write_file(target_file_name, content)


def migrate2():
    filename = sys.argv[1]

    content = read_file(filename)
    content = replace_html_tags(content)
    content = insert_redirect_to_predicate(content, filename)

    # Print to the standard output
    print(content)


if __name__ == '__main__':
    migrate2()
