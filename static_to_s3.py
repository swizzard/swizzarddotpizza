"""
Upload stuff in /static to S3
"""

import os

from boto.s3.connection import S3Connection
from boto.s3.key import Key

from miniconfig import config


def upload_to_s3(bucket, fname):
    """
    Get the basename of a file, then upload it to S3
    with the same name
    """
    key_name = os.path.basename(fname)
    key = Key(bucket)
    key.key = key_name
    key.set_contents_from_filename(fname)
    key.set_canned_acl('public-read')


def get_bucket():
    """
    Get our bucket object
    """
    conn = S3Connection(config['aws_access_key_id'],
                        config['aws_secret_access_key'])
    bucket = conn.get_bucket('swizzarddotpizza')
    bucket.set_canned_acl('public-read')
    return bucket


if __name__ == '__main__':
    # pylint: disable=invalid-name
    bkt = get_bucket()
    for fil in os.listdir('static'):
        upload_to_s3(bkt, os.path.join('static', fil))

