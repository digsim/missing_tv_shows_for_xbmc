Installation
====================

From Download
--------------

The simplest way to use *missingtvshows* is to download the packaged *pex* file from `mtvs`_ and put it somewhere on the path like ``/usr/local/bin/``or ``/usr/local/share/bin``or ``~/.local/bin/`` and make it executable,

From this point on, the binary can be executed by calling the *pex* file directly. There exist 3 variants of the *pex* file, depending on the availalbe python version. Choose either *adnitc26.pex*, *adnitc27.pex* or *adnitc35.pex* depending on what is availalbe on your system.

.. only:: builder_html

    Download files directly from here:

    * :download:`missingtvshows_.pex <../dist/missingtvshows_.pex>` For Python > 3.10

From pip
---------

Simply run::

    pipx install missingTvShows


From Sources
-------------

Final installation
^^^^^^^^^^^^^^^^^^

From a terminal launch::

    pip install .

This will compile and install the project to the pyhton libraries (eg. ``/usr/local/lib/python3.12/site-packages/missingTvShows-1.2.2.dev51+gf5133b9.d20240930.dist-info``). Furthermore it will install a script in ``/usr/local/bin/``:
* missingtvshows

Upon the first start a copy of a pristine application and logging configuration are created in the user's home directory ``~/.MissingTVShows/``. From this point on configuration files are read from this location. It is however possible to overwrite them either by placing a file with the same name (but prefixed with a dot eg. ``.logging.conf``) in the current working directory.

Development installation
^^^^^^^^^^^^^^^^^^^^^^^^

from a terminal launch::

    pip install -e .

does the same as before but, uses links instead of copying files.

Clean Working directory
^^^^^^^^^^^^^^^^^^^^^^^^

To clean the working directory::

    python setup.py clean --all
    rm -rf build/ dist/


Release Software
-----------------

Version numbers are derived from the git history with `setuptools_scm <https://github.com/pypa/setuptools-scm>`_: Likely `python -m setuptools_scm` prints the current version. It's a mix from the version of the last git tag plus the `dev` suffix with a number indicating the distance to the last git tag. If the command is called on a commit with a git tag then it just takes that tag.

The releasing itself is done with `twine <https://twine.readthedocs.io/en/latest/index.html>`_

* Build the software: `python -m build` (if not using `tox`) for creating the packages
* Check if everything is ready for deplyoment: `python -m twine check dist/*`
* Upload artifacts: `python -m twine upload --repository pypitest --verbose dist/*`


Known Problems
--------------

SSL Problems
^^^^^^^^^^^^^

Upon running the adnitc binary you might get the following exception::

    ITC Password:
    DEBUG - Using Python 2
    DEBUG - Saving calendar to file /var/folders/j4/8bm7_nb54kl2m_9kl6k5gk880000gn/T/tmp6krkW7
    INFO - Starting new HTTPS connection (1): example.com
    INFO - Starting new HTTPS connection (1): example.com
    Traceback (most recent call last):
      File "/usr/local/bin/adnitc", line 9, in <module>
        load_entry_point('adnitc==1.0.0', 'console_scripts', 'adnitc')()
      File "/Volumes/Data/ruppena/Documents/Programming/Python/AdNITC/main/__init__.py", line 8, in main
        main.getArguments(sys.argv[1:])
      File "/Volumes/Data/ruppena/Documents/Programming/Python/AdNITC/main/mainImpl.py", line 58, in getArguments
        self.main()
      File "/Volumes/Data/ruppena/Documents/Programming/Python/AdNITC/main/main.py", line 48, in main
        self.doWork()
      File "/Volumes/Data/ruppena/Documents/Programming/Python/AdNITC/main/mainImpl.py", line 76, in doWork
        events = c.fetchCalendarEvents()
      File "/Volumes/Data/ruppena/Documents/Programming/Python/AdNITC/ITC/calendar2itc.py", line 33, in fetchCalendarEvents
        response = requests.get(self.__calendarurl, auth=(self.__username, self.__password), stream=True, verify=False, proxies=self.__proxies)
      File "/Library/Python/2.7/site-packages/requests/api.py", line 70, in get
        return request('get', url, params=params, **kwargs)
      File "/Library/Python/2.7/site-packages/requests/api.py", line 56, in request
        return session.request(method=method, url=url, **kwargs)
      File "/Library/Python/2.7/site-packages/requests/sessions.py", line 475, in request
        resp = self.send(prep, **send_kwargs)
      File "/Library/Python/2.7/site-packages/requests/sessions.py", line 596, in send
        r = adapter.send(request, **kwargs)
      File "/Library/Python/2.7/site-packages/requests/adapters.py", line 497, in send
        raise SSLError(e, request=request)
    requests.exceptions.SSLError: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:590)


This simply means that some OpenSSL libraries are too old. Start by upgrading::

    sudo -H pip install --upgrade pyOpenSSL
    sudo -H pip install --upgrade ndg-httpsclient

if that is not enough also update the following::

    sudo -H pip install --upgrade pyasn1

Proxy Problems
^^^^^^^^^^^^^^^

Installation from sources may fail behind a proxy. Thus install the requirements by hand and specify the proxy::

    sudo -H pip install --proxy=http://my.proxy.com:1234 -r requirements.txt


Uninstall
----------

Method 1 (pip)
^^^^^^^^^^^^^^

If the package was installed with ``pip`` simply run::

    pip uninstall adnitc

Method 2 (from sources)
^^^^^^^^^^^^^^^^^^^^^^^

If the packages was installed from sources::

    cat files.txt |sudo xargs rm -rf

Method 3  (from sources)
^^^^^^^^^^^^^^^^^^^^^^^^^

First find the installed package with pip and the uninstall it::

    ✔ ~/Documents/Programming/Python/AdNITC [master|✚ 1]
    19:02 $ pip3 freeze |grep adnitc
    adnitc==1.1

    ✔ ~/Documents/Programming/Python/AdNITC [master|✚ 1]
    19:02 $  pip3 uninstall adnitc
    Uninstalling adnitc-1.1:
      /usr/local/bin/adnitc
      /usr/local/lib/python3.5/site-packages/adnitc-1.1.dist-info/DESCRIPTION.rst
      /usr/local/lib/python3.5/site-packages/adnitc-1.1.dist-info/INSTALLER
      /usr/local/lib/python3.5/site-packages/adnitc-1.1.dist-info/METADATA
      /usr/local/lib/python3.5/site-packages/adnitc-1.1.dist-info/RECORD
      /usr/local/lib/python3.5/site-packages/adnitc-1.1.dist-info/WHEEL
      /usr/local/lib/python3.5/site-packages/adnitc-1.1.dist-info/entry_points.txt
      /usr/local/lib/python3.5/site-packages/adnitc-1.1.dist-info/metadata.json
      /usr/local/lib/python3.5/site-packages/adnitc-1.1.dist-info/top_level.txt
      /usr/local/lib/python3.5/site-packages/adnitc/__init__.py
      /usr/local/lib/python3.5/site-packages/adnitc/__pycache__/__init__.cpython-35.pyc
      /usr/local/lib/python3.5/site-packages/adnitc/etc/adnitc-completion.bash
      /usr/local/lib/python3.5/site-packages/adnitc/etc/adnitc.conf
      /usr/local/lib/python3.5/site-packages/adnitc/etc/logging.conf
      /usr/local/lib/python3.5/site-packages/adnitc/itc/__init__.py
      /usr/local/lib/python3.5/site-packages/adnitc/itc/__pycache__/__init__.cpython-35.pyc
      /usr/local/lib/python3.5/site-packages/adnitc/itc/__pycache__/calendar2itc.cpython-35.pyc
      /usr/local/lib/python3.5/site-packages/adnitc/itc/__pycache__/calendarEvent.cpython-35.pyc
      /usr/local/lib/python3.5/site-packages/adnitc/itc/__pycache__/itcClient.cpython-35.pyc
      /usr/local/lib/python3.5/site-packages/adnitc/itc/calendar2itc.py
      /usr/local/lib/python3.5/site-packages/adnitc/itc/calendarEvent.py
      /usr/local/lib/python3.5/site-packages/adnitc/itc/itcClient.py
      /usr/local/lib/python3.5/site-packages/adnitc/main/__init__.py
      /usr/local/lib/python3.5/site-packages/adnitc/main/__pycache__/__init__.cpython-35.pyc
      /usr/local/lib/python3.5/site-packages/adnitc/main/__pycache__/main.cpython-35.pyc
      /usr/local/lib/python3.5/site-packages/adnitc/main/__pycache__/mainImpl.cpython-35.pyc
      /usr/local/lib/python3.5/site-packages/adnitc/main/main.py
      /usr/local/lib/python3.5/site-packages/adnitc/main/mainImpl.py
    Proceed (y/n)? y
      Successfully uninstalled adnitc-1.1



To install the adnitc package, use::

  python setup.py install

If installation is successful, you will be able to import the iCalendar
package, like this::

  >>> import icalendar


Building the documentation locally
----------------------------------

To build the documentation follow these steps:

.. code-block:: bash

    $ git clone http://digsim.is-a-geek.com/rhode/AdNITC
    $ cd adnitc
    $ virtualenv-2.7 .
    $ source bin/activate
    $ pip install -r requirements_docs.txt --extra-index-url http://pypi.is-a-geek.com/simple --trusted-host pypi.is-a-geek.com
    $ cd docs
    $ make html

You can now open the output from ``_build/html/index.html``. To build the
presentation-version use ``make presentation`` instead of ``make html``. You
can open the presentation at ``presentation/index.html``.


.. _`mtvs`: https://www.andreas-ruppen.ch/
