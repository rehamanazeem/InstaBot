from distutils.core import setup
setup(
  name = 'instabot',  
  packages = ['instabot'],
  version = '0.1.0',
  license='MIT',
  description = 'With the help of this package, your chrome browser can be automated to search for hashtags, like and comment on pictures. *Note* : This package requires chromedriver as per the current version of your google chrome browser.',
  author = 'Azeem Ur Rehman',
  author_email = 'rehmanazeem915@gmail.com',
  url = 'https://github.com/rehmanazeem/instabot',
  download_url = 'https://github.com/rehamanazeem/instabot/archive/refs/tags/v0.1.0-alpha.tar.gz',
  keywords = ['instagram bot', 'task automation', 'human simulation'],
  install_requires=[
          'selenium',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
