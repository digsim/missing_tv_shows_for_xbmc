About
=====

Missing TV-Shows for Kodi is a small python utility to check which episodes are still missing. Sometimes it is hard to keep up with multiple series and keep our collections clean and full. This small script iterates over all availalbe series in Kodi and checks whether they some episodes are missing.

Introduction
------------

To find missing episodes, for each season of each series, the script asks thetvdb.com for the total amount of episodes in this particular season. Based on the response from thetvdb and the information in the local Kodi databse, the scripts computes the missing episodes.

The output is either:
* command line only. The information is structured into four parts
* CSV files. The information is spread upon three files.

The command line output is structured into the following four sections:

1. All episods unwatched & Some episodes still missing
2. Some episodes alread watched & Some episodes still missing
3. All episodes unwatched & All episodes downloaded
4. Some episodes already watched & All episodes downloaded

Since TheTVDB gets constantly updated (for running seasons), it is possible that a given season is sometimes in section 2) and sometimes in section 4). However, if the season is locked on thetvdb, the information is accurate and once a a series arrives in section 4, it will stay there.

There is no section containing complete and watched episodes as I judge this infomration not relevant here. Thus, as soon as for a given season all episodes are collected and watched, it will dissapear from the list.
