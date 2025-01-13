Usage
=================


A Sample output may be look like this::

    :src$ missingTVShows
    Acquiring necessary TV-Shows information
    [===============================================================================================     ] 95%
    ##############################################################
    ###################### Unwatched Missing #####################
    ##############################################################
    -------------------------------------------------------------------------------------------------------------------------------------------------
    |Title                                        | Season (Downloaded/Available)| Missing                                                                   |
    -------------------------------------------------------------------------------------------------------------------------------------------------
    |Gold Rush                                    : | S3  ( 2/17)| missing: 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17                        |
    -------------------------------------------------------------------------------------------------------------------------------------------------
    ###############################################################
    ######################## Watched Missing ######################
    ###############################################################
    -------------------------------------------------------------------------------------------------------------------------------------------------
    |Title                              (SeasonId)  | Season (Downloaded/Available)| Missing                                                                   |
    -------------------------------------------------------------------------------------------------------------------------------------------------
    |fernOST - Von Berlin nach Tokio    (275486  ): | S1  (10/11)| missing: 11                                                                        |
    -------------------------------------------------------------------------------------------------------------------------------------------------
    ###############################################################
    ######################## Ready to Watch #######################
    ###############################################################
    Big Rig Bounty Hunters             : Season 1  and has 8/8 Episodes
    Doomsday Preppers                  : Season 2  and has 18/18 Episodes
    Doomsday Preppers                  : Season 3  and has 14/14 Episodes
    ###############################################################
    #################### Complete and Watching ####################
    ###############################################################
    Doomsday Preppers                  : Season 1  and has watched  8/12 Episodes



Installation
-------------

From pip
^^^^^^^^^^

Simply run::

    pip install missingTVShows


From Sources
^^^^^^^^^^^^^

### Final installation

From a terminal launch::

    pip install .

this will compile and install the project to the pyhton libraries (eg. /usr/local/lib/python2.7/dist-packages/XWoT_Model_Translator-1.1-py2.7.egg). Furthermore it will install a script in /usr/local/bin/:
* missingTVShows

The basic configuration and logging.conf are copied into /etc/MissingTVShows/. Upon the first start a copy of this directory is created in the user's home directory ~/.MissingTVShows/. From this point on configuration files are read from this location. It is however possible to overwrite them either by placing a file with the same name (but prefixed with a dot eg. .logging.conf) in the user home directory or a file with the same name in the current working directory.

### Development installation

from a terminal launch::

    virtualenv -p /bin/python3.12 venv-312
    source venv-312/bin/activate.fish
    pip install -e .


does the same as before but, uses links instead of copying files.

### Clean Working directory

To clean the working directory::

    rm -rf build/ dist/


Uninstall
-----------

Via pip::

    pip uninstall missingTVShows




Configuration
--------------

Upon the first launch, the script creates the ~/.MissingTVShows/ directory containing:
* logging.conf where the logger is configured
* tvshows.cfg where the general configuration is stored. Adapt at least the <db> property and point it to the Kodi MyVideosXX.db. This file is usually found under

    * On Linux system this files is usually: /home/<username>/.kodi/userdata/Database/MyVideos93.db
    * On Mac OsX the file is found under: /Users/<username>/Library/Application Support/Kodi/userdata/Database/MyVideos93.db
    * Under Windows there must me a simliar location ;-)

* tvdbdb.db the local TheTVDB.com cache as SQLite file
