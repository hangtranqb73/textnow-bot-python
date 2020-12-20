import setuptools
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setuptools.setup(
  name='textnow-bot',
  version='1.0.0',
  description='Send TextNow messages programmatically',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/george-lim/textnow-bot-python',
  author='George Lim',
  author_email='lim.george@me.com',
  license='MIT',
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
  ],
  keywords='python playwright web automation headless textnow bot',
  packages=setuptools.find_packages(include=['textnow_bot']),
  install_requires=['playwright'],
  python_requires='>=3.7'
)
