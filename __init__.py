# -*- coding: utf-8 -*-
"""
/***************************************************************************
 treeMap
                                 A QGIS plugin
 Tree Mapping Tool
                             -------------------
        begin                : 2014-02-20
        copyright            : (C) 2014 by Thomas & Erick
        email                : e.omwandho@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


def name():
    return "Tree Mapping Tool"


def description():
    return "Tree Mapping Tool"


def version():
    return "Version 0.1"


def icon():
    return "icon.png"


def qgisMinimumVersion():
    return "1.8"

def author():
    return "Thomas & Erick"

def email():
    return "e.omwandho@gmail.com"

def classFactory(iface):
    # load treeMap class from file treeMap
    from treemap import treeMap
    return treeMap(iface)
