# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2016 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

import os
from kombu import Queue
import dj_database_url

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

SITEURL = os.getenv('SITEURL', "http://localhost:8000/")

TIME_ZONE = os.getenv('TIME_ZONE', "America/Chicago")

DATABASE_URL = os.getenv(
    'DATABASE_URL',
    'sqlite:///{path}'.format(
        path=os.path.join(PROJECT_ROOT, 'development.db')
    )
)

DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600)
}

CATALOGUE = {
    'default': {
        # The underlying CSW implementation
        # default is pycsw in local mode (tied directly to GeoNode Django DB)
        'ENGINE': 'geonode.catalogue.backends.pycsw_local',
        # pycsw in non-local mode
        # 'ENGINE': 'geonode.catalogue.backends.pycsw_http',
        # GeoNetwork opensource
        # 'ENGINE': 'geonode.catalogue.backends.geonetwork',
        # deegree and others
        # 'ENGINE': 'geonode.catalogue.backends.generic',

        # The FULLY QUALIFIED base url to the CSW instance for this GeoNode
        'URL': '%scatalogue/csw' % SITEURL,
        # 'URL': 'http://localhost:8080/geonetwork/srv/en/csw',
        # 'URL': 'http://localhost:8080/deegree-csw-demo-3.0.4/services',

        # login credentials (for GeoNetwork)
        'USER': 'admin',
        'PASSWORD': 'admin',
    }
}

# Leaflet config
LAYER_PREVIEW_LIBRARY = 'leaflet'
LEAFLET_CONFIG = {
    'TILES': [
        # Find tiles at:
        # http://leaflet-extras.github.io/leaflet-providers/preview/

        # Map Quest
        ('Map Quest',
         'http://otile4.mqcdn.com/tiles/1.0.0/osm/{z}/{x}/{y}.png',
         'Tiles Courtesy of <a href="http://www.mapquest.com/">MapQuest</a> '
         '&mdash; Map data &copy; '
         '<a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'),
        # Stamen toner lite.
        # ('Watercolor',
        #  'http://{s}.tile.stamen.com/watercolor/{z}/{x}/{y}.png',
        #  'Map tiles by <a href="http://stamen.com">Stamen Design</a>, \
        #  <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; \
        #  <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, \
        #  <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>'),
        # ('Toner Lite',
        #  'http://{s}.tile.stamen.com/toner-lite/{z}/{x}/{y}.png',
        #  'Map tiles by <a href="http://stamen.com">Stamen Design</a>, \
        #  <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; \
        #  <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, \
        #  <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>'),
    ],
    'PLUGINS': {
        'esri-leaflet': {
            'js': 'lib/js/esri-leaflet.js',
            'auto-include': True,
        },
        'leaflet-fullscreen': {
            'css': 'lib/css/leaflet.fullscreen.css',
            'js': 'lib/js/Leaflet.fullscreen.min.js',
            'auto-include': True,
        },
    },
    'SRID': 3857,
    'RESET_VIEW': False
}

# Legacy from Geoserver
OGC_SERVER = {
    'default': {
        'LOCATION': SITEURL + 'qgis-server/',
        'PUBLIC_LOCATION': SITEURL + 'qgis-server/',
        'LOG_FILE': '/tmp/qgis-server.log'
    }
}

# OGC (WMS/WFS/WCS) Server Settings
tiles_directory = os.path.join(PROJECT_ROOT, "qgis_tiles")
QGIS_SERVER_CONFIG = {
    'tiles_directory': tiles_directory,
    'tile_path': tiles_directory + '/%s/%d/%d/%d.png',
    'legend_path': tiles_directory + '/%s/legend.png',
    'thumbnail_path': tiles_directory + '/%s/thumbnail.png',
    'map_tile_path': os.path.join(
        tiles_directory, '%s', 'map_tiles', '%s', '%s', '%s', '%s.png'),
    'qgis_server_url': os.getenv('QGIS_SERVER_URL', 'http://127.0.0.1/cgi-bin/qgis_mapserv.fcgi'),
    'layer_directory': os.path.join(PROJECT_ROOT, "qgis_layer")
}
