from setuptools import setup, find_packages

setup(
   name='dir-tree-drh',
   version='1.5',
   packages=find_packages(),
   description="Creating a directory tree is an efficient method for visually organizing your project's directory structure, complete with detailed information. It provides a clear model of your project layout for easy reference and management.",
   long_description=open('README.md', encoding='utf-8').read(),
   long_description_content_type='text/markdown',
   author='dragon-devs',
   author_email='dragonfourtyseven@email.com',
   url='https://github.com/dragon-devs/dir-tree-drh',
   license='MIT',
   classifiers=[
      'Programming Language :: Python :: 3',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
   ],
   entry_points={
      'console_scripts': [
         'dir-tree = dir_tree.main:main'
      ]
   }
)
