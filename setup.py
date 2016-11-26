
#!/usr/bin/env python3
from distutils.core import setup
import sys
import os.path

lumber_description = "Calculates the material cost for various tool and furniture projects by checking the need for each project against the estimated cost in lumber."

setup(name = 'lumbercalc',
        version = '0.1',
        author = 'Kenneth P. J. Dyer',
        author_email = 'kenneth@avoceteditors.com',
        url = 'https://github.com/kennethpjdyer/lumber-calc',
        description = lumber_description,
        license = 'BSD 3-clause',
        packages = ['lumbercalc'],
        scripts = ['scripts/lumber-calc'],
        classifiers = [
            'Development Status :: 2 - Pre-Alpha',
            'Environment :: Console'],
        data_files = []
)
