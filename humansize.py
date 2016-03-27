SUFFIXES = {1000:['KB','MB','TB','GB','PB','EB','ZB','YB'],
            1024:['KiB','MiB','TiB','GiB','PiB','EiB','ZiB','YiB']}

def approximat_size(size, a_kilobyte_is_1024_bytes=True):
    ''' Convert file size into human readable form

        Keyword arguments:
        size --- file size in bytes
        a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                    if False, use multiples of 1000

        Returns: string

        '''

    if size < 0:
        raise ValueError('number must be non negative')

    multple = 1024 if a_kilobyte_is_1024_bytes else 1000

    for suffix in SUFFIXES [multple]:
        size /= multple
        if size < multple:
            return '{0:.1f}{1}'.format(size, suffix)

    raise ValueError ('number too large')

if __name__ == '__main__':
    print(approximat_size(1000000000000,False))
    print(approximat_size(1000000000000))
