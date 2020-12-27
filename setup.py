import setuptools
import pathlib

setuptools.setup(
  name='textnow-bot',
  version='1.0.1',
  description='Send TextNow messages programmatically',
  long_description=pathlib.Path(__file__).parent.joinpath('README.md').read_text(),
  long_description_content_type='text/markdown',
  url='https://github.com/george-lim/textnow-bot-python',
  author='George Lim',
  author_email='lim.george@me.com',
  license='MIT',
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Internet',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9'
  ],
  keywords='python playwright web automation headless textnow bot',
  packages=setuptools.find_packages(),
  install_requires=['playwright==0.171.0'],
  python_requires='>=3.7'
)
