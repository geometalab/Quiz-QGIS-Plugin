# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TestGame
                                 A QGIS plugin
 test for quiz
                             -------------------
        begin                : 2013-12-19
        copyright            : (C) 2013 by rkrucker
        email                : rafael_krucker@hotmail.com
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
def classFactory(iface):
    # load TestGame class from file TestGame
    from testgame import TestGame
    return TestGame(iface)
