from setuptools import setup #, find_packages

setup(
    name='valence',
    version='1.2',
    description='A package for Estonian language text valence(positive/negative) detection',
    scripts=['bayes.py', 'valencecolor.py'],
    packages=['valence'],
    install_requires=['nltk>=3.7'],
    include_package_data=True,
    url='www.eki.ee',
    author='Institute of the Estonian Language',
    author_email='ekorpus@eki.ee',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Linguistic',
        'Natural Language :: Estonian',
    ],
    keywords='estonian valence',
    license='GPLv3',
    zip_safe=False
)
