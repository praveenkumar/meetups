=======================
Lets Talk about systemd
=======================

.. image:: images/what_is_systemd.png
    :height: 500px
    :width: 600px
    :scale: 50%
    :align: center

:Name: Praveen Kumar
:Contact: kumarpraveen [AT] fedoraproject DOT org
:Date: 2015-04-25


Agenda
======

- What is systemd
- What capabilities it provides
- How to use systemd
- How a service file looks like
- Intro about systemd-nspawn
- Resources


What is systemd
===============

- Modular
- Asynchronous and concurrent
- features a fully language-agnostic API


systemd Cont...
===============

.. image:: images/systemd_parallel.jpg
    :height: 600px
    :width: 700px
    :scale: 70%
    :align: center


How to use systemd
==================

- Default init system for CentOS
- List out units

  + systemctl list-units

- List out services

  + systemctl list-units --type service
  + systemctl list-units --type service --all


How to use systemd cont...
==========================

- List out targets

  + systemctl list-units --type targets

- Check CGroup tree

  + systemd-cgls

Service file Template
=====================

::

    [Unit]
    Description=The Apache HTTP Server
    After=network.target remote-fs.target nss-lookup.target

    [Service]
    Type=notify
    Environment=LANG=C
    ExecStart=/usr/sbin/httpd $OPTIONS -DFOREGROUND
    ExecReload=/usr/sbin/httpd $OPTIONS -k graceful
    # Send SIGWINCH for graceful stop
    KillSignal=SIGWINCH
    KillMode=mixed
    PrivateTmp=true

    [Install]
    WantedBy=multi-user.target


sysemd-nspawn
=============

- systemd-nspawn is a small utility which is use to create light weight containers
- Setup a container

::

    $ sudo yum -y --nogpg --releasever=7 --installroot=/srv/mycontainer \
    install systemd passwd yum vim-minimal


sysemd-nspawn cont...
=====================

- Setup container password

::

    $ sudo systemd-nspawn -D /srv/mycontainer

- Start a container

::

    $ sudo systemd-nspawn -jbD /srv/mycontainer


Resources
=========
- http://www.freedesktop.org/wiki/Software/systemd


Thank You
=========
