=======================
Data Container Madness
=======================

Your data should be outlives the brief lifetime of a container.

:name: Praveen Kumar
:contact: kumarpraveen [AT] fedoraproject DOT org
:date: 2015-04-25


Agenda
======

- What is data container
- Why data container
- How to create one
- How to take backup
- How to restore data
- Demo


Data-Container
==============

- Docker volumes, and data it contain survive as long as any container reference
  them.


WHY data-container
==================

- Containers do not persist data across invocations.
- Enable portability
- Easy to update service containers without lossing data
- No need to maintain permission with host.

Data-container creation
=======================

- $ docker run -v /data busybox /bin/sh

Data-container backup
=====================

- $ docker docker run -rm --volumes-from DATA -v $(pwd):/backup busybox tar cvf
  /backup/backup.tar /data


Data-container restore
======================

- $ docker run -v /data -name DATA2 busybox true
- $ docker run -rm --volumes-from DATA2 -v $(pwd):/backup busybox tar xvf
  /backup/backup.tar data/


Demo Time
=========

- Source: https://github.com/praveenkumar/meetups
- Images: https://registry.hub.docker.com/repos/kumarpraveen/

Questions
=========
**?**

Thank You
=========
