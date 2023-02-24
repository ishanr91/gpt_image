from setuptools import setup, find_packages

setup(
    name='gpt_image',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gpt_image=gpt_image.main:main'
        ]
    },
    install_requires=[
        'torch>=1.7.0',
        'torchvision>=0.8.1',
        'numpy>=1.19.5',
        'Pillow>=8.0.1',
        'requests>=2.25.1',
        'tqdm>=4.51.0',
        'argparse>=1.1'
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='Description of your package',
    url='https://github.com/your-username/your-package',
)

