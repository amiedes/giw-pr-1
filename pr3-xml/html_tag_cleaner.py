#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""

class HtmlTagCleaner:

    substitutions = {
        '<p>': '',     '</p>': '\n',
        '<a>': '',     '</a>': '',
        '<h3>': '\n',  '</h3>': '\n--------------------\n',
        '<div>': '',   '</div>': '',
        '<strong>': '', '</strong>': '',
        '<span>': '',   '</span>': ''
    }

    @classmethod
    def clean(self, dirty_text):
        dirty_text.replace('\n', '')

        clean_text = ""
        current_tag = ""
        reading_tag = False

        for c in dirty_text:
            # si estamos dentro de un tag
            if reading_tag:
                current_tag += c
                # si detectamos el final del tag, realizar sustitución
                if c == '>':
                    if current_tag in self.substitutions:
                        clean_text += self.substitutions[current_tag]
                    reading_tag = False
                    current_tag = ""
            # si no estamos dentro de un tag
            else:
                if c == '<':
                    reading_tag = True
                    current_tag += c
                else:
                    clean_text += c
        return clean_text
