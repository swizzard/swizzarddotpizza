"""
Convert our markdown sections to html so they can be `include`d by jinja2
"""

import markdown


def section_to_html(section):
    """
    Convert a markdown file in the markdown folder and convert it
    into a template snippet in the templates folder
    """
    md_fil_name = 'markdown/{}.md'.format(section)
    html_fil_name = 'templates/{}.html'.format(section)
    markdown.markdownFromFile(input=md_fil_name, output=html_fil_name)

if __name__ == "__main__":
    from miniconfig import config
    for section_name in config['section_names'].split():
        section_to_html(section_name)

