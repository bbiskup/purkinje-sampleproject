from setuptools import setup

readme = open('README.rst').read()
changes = open('CHANGES.rst').read()



def parse_requirements():
    with open('requirements.txt') as req:
        return [x.strip() for x in req.readlines()
                if not x.startswith('-e') and
                not x.startswith('git+') and
                not x.startswith('https://')]


def parse_dependency_links():
    with open('requirements.txt') as req:
        return [x.strip() for x in req.readlines()
                if x.startswith('https://')]


setup(name='purkinje-sampleproject',
      version='0.1.2',
      description='Sample project for purkinje test runner',
      long_description=readme + '\n\n' + changes,
      author='Bernhard Biskup',
      author_email='bbiskup@gmx.de',
      url='https://github.com/bbiskup/purkinje-sampleproject/',
      package_dir={'purkinje_sampleproject': 'purkinje_sampleproject'},
      packages=['purkinje_sampleproject'],
      zip_safe=False,
      include_package_data=True,
      install_requires=parse_requirements(),
      classifiers={
          'Development Status :: 2 - Pre-Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          # Topic :: Software Development :: Libraries :: Python Modules',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.5',
      },
      license='The MIT License (MIT)',
      keywords='purkinje pytest',
      tests_require=['tox'],
      )
