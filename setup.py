from setuptools import setup, find_packages


required = ['opencv-python',
            'pypylon']

try:
    setup(
        name                = 'camapislib',
        version             = '1.0.0',
        description         = 'camera library',
        author              = '',
        author_email        = '',
        url                 = '',
        download_url        = '',
        script_args         = ["bdist_wheel", "clean", "--all"],
        install_requires    = required,
        packages            = find_packages(exclude=['tests*']),
        keywords            = [''],
        python_requires     = '',
        zip_safe            = False
    )
except Exception as e:
    print(e)
