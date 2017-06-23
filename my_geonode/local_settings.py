# -*- coding: utf-8 -*-
import os
import geonode

# Setting debug to true makes Django serve static media and
# present pretty error pages.
DEBUG = TEMPLATE_DEBUG = True

# Set to True to load non-minified versions of (static) client dependencies
# Requires to set-up Node and tools that are required for static development 
# otherwise it will raise errors for the missing non-minified dependencies
DEBUG_STATIC = False

SITENAME = 'GeoPortal-CIEFAP-NODOBAP'
SITEURL = 'http://192.168.0.56/'

DATABASE_ENGINE = 'postgresql_psycopg2'
DATABASE_NAME = 'geonode'
DATABASE_USER = 'geonode'
DATABASE_PASSWORD = 'XXXXXXXXXXXXXXXXXXXXXX'
DATABASE_HOST = 'localhost'
DATABASE_PORT = '5432'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
    },
    'datastore': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'geonode_data',
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
    }
}

GEOSERVER_URL = SITEURL + 'geoserver/'

# OGC (WMS/WFS/WCS) Server Settings
OGC_SERVER = {
    'default' : {
        'BACKEND' : 'geonode.geoserver',
        'LOCATION' : 'http://192.168.0.56:8080/geoserver/',
        'PUBLIC_LOCATION' : GEOSERVER_URL,
        'USER' : 'admin',
        'PASSWORD' : 'XXXXXXXXXXXXXXXXXXxxxxx',
        'MAPFISH_PRINT_ENABLED' : True,
        'PRINT_NG_ENABLED' : True,
        'GEONODE_SECURITY_ENABLED' : True,
        'GEOGIG_ENABLED' : False,
        'WMST_ENABLED' : False,
        'BACKEND_WRITE_ENABLED': True,
        'WPS_ENABLED' : True,
        'LOG_FILE':'/usr/share/geoserver/data/logs/geoserver.log',
        # Set to name of database in DATABASES dictionary to enable
        'DATASTORE': 'datastore',
        'LOGIN_ENDPOINT': 'j_spring_oauth2_geonode_login',
        'LOGOUT_ENDPOINT': 'j_spring_oauth2_geonode_logout',
    }
}

LANGUAGE_CODE = 'en'

MEDIA_ROOT = '/var/www/geonode/uploaded'
STATIC_ROOT = '/var/www/geonode/static/'

# secret key used in hashing, should be a long, unique string for each
# site.  See http://docs.djangoproject.com/en/1.2/ref/settings/#secret-key
SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXxx'


CATALOGUE = {
    'default': {
        # The underlying CSW backend
        # ("pycsw_http", "pycsw_local", "geonetwork", "deegree")
        'ENGINE': 'geonode.catalogue.backends.pycsw_local',
        # The FULLY QUALIFIED base url to the CSW instance for this GeoNode
        'URL': '%scatalogue/csw' % SITEURL,
    }
}

# A Google Maps API key is needed for the 3D Google Earth view of maps
# See http://code.google.com/apis/maps/signup.html
GOOGLE_API_KEY ="AIzaSyCx53BSXM4RbG-Gzs9SaXFLQYxxjR8ZIg4"
BING_API_KEY ="Anh26u7_QPVu8VLSyvt4AkZEKoY7PJ8pQvKppervUt_fdt9UG77NiKP2FDgqdg8y"

MAP_BASELAYERS = [{
    "source": {"ptype": "gxp_olsource"},
    "type": "OpenLayers.Layer",
    "args": ["No background"],
    "visibility": False,
    "fixed": True,
    "group":"background"

},{
    "source": {"ptype":"gxp_googlesource",
        "apiKey": GOOGLE_API_KEY
    },
   "group":"background",
   "name":"SATELLITE",
   "visibility": False,
   "fixed": True,

},{
"source": {
           "ptype":"gxp_bingsource",
           "apiKey": BING_API_KEY
          },
"group":"background",
"name":"Aerial",
"visibility": False,
"fixed": True,

}, {
    "source": {"ptype": "gxp_osmsource"},
    "type": "OpenLayers.Layer.OSM",
    "name": "mapnik",
    "visibility": True,
    "fixed": True,
    "group": "background"
}]

GEONODE_ROOT = os.path.dirname(geonode.__file__)

TEMPLATE_DIRS = (
    '/etc/geonode/templates',
    os.path.join(GEONODE_ROOT, 'templates'),
)

# Additional directories which hold static files
STATICFILES_DIRS = [
    '/etc/geonode/media',
    os.path.join(GEONODE_ROOT, 'static'),
]

REGISTRATION_OPEN = True
ACCOUNT_APPROVAL_REQUIRED = False

ACCOUNT_EMAIL_CONFIRMATION_EMAIL = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True

# Allowed values for the preview library are 'geoext' and 'leaflet'.
LAYER_PREVIEW_LIBRARY = 'geoext'

# Uncomment the following to receive emails whenever there are errors in GeoNode
# or to be notified of new user requests when ACCOUNT_APPROVAL_REQUIRED has been set.
#ADMINS = (
#            ('John', 'john@example.com'), 
#         )

# Uncomment the following to use a Gmail account as the email backend
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'geop.adm1@gmail.com'
EMAIL_HOST_PASSWORD = 'XXXXXXXXXXXXXXXXXXXXXXXxxx'
EMAIL_PORT = 587

#ACCOUNT_NOTIFY_ON_PASSWORD_CHANGE = True

SEARCH_FILTERS = {
    'TEXT_ENABLED': True,
    'TYPE_ENABLED': True,
    'CATEGORIES_ENABLED': True,
    'OWNERS_ENABLED': True,
    'KEYWORDS_ENABLED': True,
    'DATE_ENABLED': True,
    'REGION_ENABLED': True,
    'EXTENT_ENABLED': True,
}

# default map projection
# Note: If set to EPSG:4326, then only EPSG:4326 basemaps will work.
DEFAULT_MAP_CRS = "EPSG:900913"

# Where should newly created maps be focused?
DEFAULT_MAP_CENTER = (-68, -46)

# How tightly zoomed should newly created maps be?
# 0 = entire world;
# maximum zoom is between 12 and 15 (for Google Maps, coverage varies by area)
DEFAULT_MAP_ZOOM = 5

# Whether the uplaoded resources should be public and downloadable by default or not
#DEFAULT_ANONYMOUS_VIEW_PERMISSION = True
#DEFAULT_ANONYMOUS_DOWNLOAD_PERMISSION = False

# Topic Categories list should not be modified (they are ISO). In case you
# absolutely need it set to True this variable
#MODIFY_TOPICCATEGORY = strtobool(os.getenv('MODIFY_TOPICCATEGORY', 'False'))

# For more information on available settings please consult the Django docs at
# https://docs.djangoproject.com/en/dev/ref/settings
ALLOWED_HOSTS=['localhost', '192.168.0.56', ]
PROXY_ALLOWED_HOSTS = ('localhost', '::1','http://www.isotc211.org/','http://ambiente.caearte.conae.gov.ar','http://sig.se.gob.ar/','http://ide.agroindustria.gob.ar','http://sipan.inta.gov.ar/','http://www.catastro.chubut.gov.ar/','http://geointa.inta.gov.ar/','http://geo2.ambiente.gob.ar/','www.ide.siia.gov.ar/','www.geoservicios.conae.gov.ar/','http://geo2.ambiente.gob.ar/','https://firms.modaps.eosdis.nasa.gov/', )

SILENCED_SYSTEM_CHECKS = ['1_8.W001', 'fields.W340']
