from setuptools import setup

readme = open('README.rst').read()
changes = open('CHANGES.rst').read()


def parse_requirements():
    with open('requirements.txt') as req:
        return [x for x in req.readlines() if not x.startswith('-e ')]


setup(name='flotsam',
      version='0.1.0',
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
          'Programming Language :: Python :: 3.4',
      },
      license='The MIT License (MIT)',
      keywords='flotsam utilities',
      tests_require=['tox'],
      )
