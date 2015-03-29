# -*- coding: utf-8 -*-
"""The :mod:`valence` contains text valence related methods."""
import os
import cgi
from ekorpus.lib.base import *
from valencecolor import marktext

class ValenceController(BaseController):

    def index(self):
        """Generates the text input form."""
        return render('/valence/valence.mak')

    def color(self):
        """Count and mark with a color the valence keywords."""
        p = request.params

        dataonly="" 
        if 'dataonly' in p:
            dataonly = p['dataonly']

        lexiconbased="" 
        if 'lexiconbased' in p:
            lexiconbased = p['lexiconbased']

        if ('text' in p) and p['text']:
            c.text=marktext(p['text'], dataonly, lexiconbased)
        else:
            c.text = "Nothing"

        if dataonly:
            return c.text
        else:
            c.lexiconbased = lexiconbased
            return render('/valence/colored.mak')

