#!/usr/bin/env python

# TODO:
# * Get feedback working from the help doamin
# * write something to deal with re-generating the index for the js search
# * hand edits:
#   * Edit some long titles down to shorter versions
# DONE:
# * redirects from old wiki
# * Find other feedback links to link to
# * check the link target for the "I want to suggest a new guide" - it fires
# *   up the JS for feedback
# * styling/theme
# * header and footer
# * check that all pages are linked to
# * sublinks
# * check that all links work
# * escaped entities in titles - see SaveAndRunPythonVersion
# * search
#  check images and icons
#  rename /stories url to articles or something
#  create index page on /
#  handle in-page links on index_page (and other pages?)
#  finish TOCs
#  fix internal links from TOC - they are preceded with a . which borks if
#    you access the page without a trailing slash


import codecs
import html2text
import HTMLParser
import mistune
import os
import re
import sys

header_template = """
<!--
.. title: {title}
.. slug: {slug}
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->


"""


page_titles = {
    'TypesOfConsoles.html':  'Types of consoles',
    'FileEditor.html': 'File editor',
    'ConfigFiles.html': 'Config files',
    'ExternalVCS.html': 'External VCS',
    '403ForbiddenError.html': '403 Forbidden error',
    'ImportingYourLocalDatabaseToPythonAnywhere.html': 'Importing your local database to PythonAnywhere',
    'KindsOfDatabases.html': 'Kinds of databases',
    'SingleLineConsoleProblem.html': 'Single line console problem',
    'MigatingWeb2pyFromSQLiteToMySQL.html': 'Migating Web2py from SQLite to MySQL',
    'Python3WebApps.html': 'Python3 webapps',
    'Haskell.html': 'Haskell',
    'FileBrowser.html': 'File browser',
    'MultipleDomainsWeb2py.html': 'Multiple domains with Web2py',
    'VirtualEnvForNewerDjango.html': 'VirtualEnv for newer Django',
    'Using(20)SQLAlchemy(20)with(20)MySQL.html': 'Using SQLAlchemy with MySQL',
    'Buffering.html': 'Buffering',
    'ForcingHTTPS.html': 'Forcing HTTPS',
    'WebAppBasics.html': 'Webapp basics',
    'Javascript.html': 'Javascript',
    'ScheduledTasks.html': 'Scheduled tasks',
    'BadContent.html': 'Bad content',
    'MySQLDatabaseSize.html': 'MySQL database size',
    'UsingMySQL.html': 'Using MySQL',
    'ReloadWebApp.html': 'Reload webapp',
    'LongRunningTasks.html': 'Long running tasks',
    'ChangingFontSize.html': 'Changing font size',
    'ChangingConsolesName.html': "Changing a console's Name",
    'DatabaseCharacterSets.html': 'Database character sets',
    'UsingDropbox.html': 'Using Dropbox',
    'NakedDomains.html': 'Naked domains',
    'SMTPForFreeUsers.html': 'SMTP for free users',
    'ScheduledTaskParameters.html': 'Scheduled task parameters',
    'LoadDataInfile.html': 'LoadDataInfile',
    'Using(20)Tornado.html': 'Using tornado',
    'TypingProblemsInternational.html': 'Typing problems international',
    'DjangoTutorial.html': 'Django tutorial',
    'UsingANewDomainForExistingWebApp.html': 'Using a new domain for existing webapp',
    'SSHTunnelling.html': 'SSH tunnelling',
    'InstallingNewModules.html': 'Installing new modules',
    'StartingEncryptedConnection.html': 'Starting encrypted connection',
    'PythonAnywhere.html': 'PythonAnywhere',
    'AdminIsDisabledBecauseInsecureChannel.html': 'Admin is disabled because insecure channel',
    'ICantSeeWhatIAmTyping.html': "I can't see what I'm typing",
    'MatplotLibGraphs.html': 'MatplotLib graphs',
}



_escape_pattern = re.compile(r'&(?!#?\w+;)')


def escape(text, quote=False, smart_amp=True):
    """Replace special characters "&", "<" and ">" to HTML-safe sequences.
    The original cgi.escape will always escape "&", but you can control
    this one for a smart escape amp.
    :param quote: if set to True, " and ' will be escaped.
    :param smart_amp: if set to False, & will always be escaped.
    """
    if smart_amp:
        text = _escape_pattern.sub('&amp;', text)
    else:
        text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    if quote:
        text = text.replace('"', '&quot;')
        text = text.replace("'", '&#39;')
    return text




def indent(text, indent_with="    "):
    lines = text.splitlines()
    indented = []
    for line in lines:
        if line.strip():
            indented.append(indent_with + line)
        else:
            indented.append(line)
    indented = '\n'.join(indented)
    return indented


class MarkdownRenderer(object):
    """Render markdown to markdown
    """

    def __init__(self, **kwargs):
        self.list_id = None
        self.options = kwargs
        self.links = set()

    def placeholder(self):
        return ''

    def block_code(self, code, lang=None):
        lang_spec = ""
        if lang is not None:
            lang_spec = indent(":::" + lang)
        return "\n" + lang_spec + indent(code) + "\n"


    def block_quote(self, text):
        return indent("\n" + text + "\n", "> ")

    def block_html(self, html):
        return "\n" + html + "\n"

    def header(self, text, level, raw=None):
        marker = "#" * level
        if raw:
            return "\n\n" + marker + raw + "\n\n"
        return "\n\n" + marker + text + "\n\n"

    def hrule(self):
        return "\n" + ("-" * 80) + "\n"

    def list(self, body, ordered=True):
        bullet = "  * "
        if ordered is True:
            bullet = "  1. "
        return "\n" + body.replace("\n\n", "\n").replace("  * ", "    * ").replace("  1. ", "    1. ").replace("<li>", bullet)


    def list_item(self, text):
        return "<li>" + text + "\n"

    def paragraph(self, text):
        return "\n" + text + "\n"

    def table(self, header, body):
        # TODO - probably need to add a header separator
        return "\n" + header + "\n" + body + "\n"

    def table_row(self, content):
        return content + "\n"

    def table_cell(self, content, **flags):
        # TODO: May need to handle alignment
        return "| " + content + "|"

    def double_emphasis(self, text):
        return "**" + text + "**"

    def emphasis(self, text):
        return "*" + text + "*"

    def codespan(self, text):
        return "`" + text + "`"

    def linebreak(self):
        # TODO: not sure about this
        return "  \n"

    def strikethrough(self, text):
        return "~~" + text + "~~"

    def text(self, text):
        return text

    def autolink(self, link, is_email=False):
        return "<{}>".format(link)


    def link(self, link, title, text):
        delinks = set([
            "PythonAnywhere",
            "JavaScript",
            "OperationalError",
            "NicholasMurray",
            "http://my_username.pythonanywhere.com/admin",
        ])
        if text in delinks:
            return text
        if link.endswith(".html"):
            link = link[:-5]
            if link.startswith("./"):
                link = "/pages" + link[1:]
        if text == "I want to suggest a new button to go here":
            text = "I want to suggest a new guide to go here"
        if link.startswith("http:"):
            link = link[5:]
        if link.startswith("/task_helpers/"):
            link = "//www.pythonanywhere.com" + link

        conversions = {
            "/pages/VirtualenvForNewerDjango": "/pages/VirtualEnvForNewerDjango",
            "/pages/CherryPy": "//www.cherrypy.org/",
            "/pages/GitHub": "//www.github.com/",
            "/pages/BitBucket": "//www.bitbucket.org/",
            "/pages/Web2Py": "//www.web2py.com/",
            "/pages/PythonAnywhere": "https://www.pythonanywhere.com/",
            "/pages/PythonAnywere": "https://www.pythonanywhere.com/",
            "/pages/GoDaddy": "//www.godaddy.com/",
            "/pages/Educationaccount": "https://www.pythonanywhere.com/account",
            "/pages/Flaskweb_app_setup": "https://www.pythonanywhere.com/web_app_setup",
            "/pages/Flaskconsoles": "https://www.pythonanywhere.com/consoles",
            "/pages/FollowingTheDjangoTutorialweb_app_setup": "https://www.pythonanywhere.com/web_app_setup",
            "http://tutorial.pythonanywhere.com/static/django/new_folder_for_templates.png": "//tutorial.pythonanywhere.com/static/django/new_folder_for_templates.png",
        }
        if link in conversions:
            link = conversions[link]
        self.links.add(link)
        if title:
            return "[{}]({} \"{}\")".format(text, link, title)
        return "[{}]({})".format(text, link)

    def image(self, src, title, text):
        if src.endswith("smile.png"):
            src = "/smile.png"
        if src.endswith("students_dropdown.png"):
            src = "/students_dropdown.png"
        if src.startswith("/static/"):
            src = "//www.pythonanywhere.com" + src
        if title:
            return "![{}]({} \"{}\")".format(text, src, title)
        return "![{}]({})".format(text, src)

    def inline_html(self, html):
        return html

    def newline(self):
        return '\n'

    def footnote_ref(self, key, index):
        return "[^{}]".format(key)

    def footnote_item(self, key, text):
        return "[^{}]: {}".format(key, text)

    def footnotes(self, text):
        return text


def fixtocs(md):
    md = re.sub(r"Contents\n\n.*?\n\n", r"\n\n#Contents\n[TOC]\n\n", md, flags=re.DOTALL)
    return md


def convert_file(filename):
    html_parser = HTMLParser.HTMLParser()
    h = html2text.HTML2Text()
    h.body_width = 0
    renderer = MarkdownRenderer()
    processor = mistune.Markdown(renderer=renderer)

    slug = filename.replace(".html", "").replace("(20)", "")
    output_filename = filename.replace(".html", ".md").replace("(20)", "")

    with codecs.open(os.path.join("originalhtml", filename), "r", "utf-8") as inf:
        markdown = h.handle(inf.read())
    markdown = markdown.split("* * *")[1]
    markdown = fixtocs(markdown)
    markdown = markdown.replace(r"\(20\)", "")
    markdown = markdown.replace(r"\(2f\)", "")

    if markdown.lstrip().startswith("# "):
        title = markdown.lstrip().split("\n")[0].replace("# ", "")
        markdown = "\n".join(markdown.lstrip().split("\n")[1:])
    else:
        title = page_titles[filename]
    title = html_parser.unescape(title)

    markdown = processor(markdown)

    replacements = [
        ("*<https://>*", "`<https://>`"),
        ("*svn+<ssh://>*", "`svn+<ssh://>`"),
        ("[/consoles/](https://www.pythonanywhere.com/consoles)(Bash Console)", " new Bash console from your [Dashboard](https://www.pythonanywhere.com/consoles)"),
        ("        from django.core.wsgi import get_wsgi_application", "    from django.core.wsgi import get_wsgi_application"),
        ("  * \nIf you're using a version of Django", "If you're using a version of Django"),
        ("new button to go here. ]()", "new button to go here. ](){: .feedback_link}"),
    ]
    for replacement in replacements:
        markdown = markdown.replace(*replacement)

    with codecs.open(os.path.join("articles", output_filename), "w", "utf-8") as of:
        of.write(header_template.format(
            title=title,
            slug=slug
        ))
        of.write(markdown)
    return output_filename, renderer.links


if __name__ == "__main__":
    if len(sys.argv) == 1:
        links = set()
        file_links = set()
        for filename in os.listdir("originalhtml"):
            if filename.endswith(".html"):
                print "Converting", filename
                output_filename, new_links = convert_file(filename)
                links.update(new_links)
                file_links.add("/pages/" + output_filename.replace(".md", ""))

        reports = []

        for file_link in file_links:
            if file_link not in links:
                reports.append("%s not linked to" % (file_link,))
        if reports:
            print "******* Some pages are not linked to:"
            print "\n".join(reports)
    else:
        print "Converting", sys.argv[1]
        convert_file(sys.argv[1])
