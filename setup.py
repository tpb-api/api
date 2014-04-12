from setuptools import setup

import os

# Put here required packages or
# Uncomment one or more lines below in the install_requires section
# for the specific client drivers/modules your application needs.
packages = ['Django<=1.6',
            'static3',  # If you want serve the static files in the same server
            # 'mysql-connector-python',
            # 'pymongo',
            # 'psycopg2',
           ]

if 'REDISCLOUD_URL' in os.environ and 'REDISCLOUD_PORT' in os.environ and 'REDISCLOUD_PASSWORD' in os.environ:
     packages.append('django-redis-cache')
     packages.append('hiredis')

setup(
    name='TPBApi',
    version='1.0',
    description='a TPB API',
    author='tpb',
    author_email='tpb.api@gmail.com',
    url='https:/github.com/tpb-api/api',
    install_requires=['Django>=1.4'],
)
