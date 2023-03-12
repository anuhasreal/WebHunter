### Welcome To AlienBot Database ###
import socket as s
import re
import subprocess
import json
import sys , urllib.request , os, time
import sys
import requests
import pandas as pd
import urllib
import time
import pyspeedtest
import requests
import urllib as urllib1
import json
import requests
import pandas as pd
import urllib
import time
#from google.colab import files#
import io 
import requests
import socket
import geocoder
import whois
from datetime import datetime
import pyfiglet
from os import system, name
mainName = "                     Created by Kaveesha Anuhas"
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[92m'
    MAIN = '\033[95m'
    MAIN1 = '\033[96m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
# read all subdomains
file = open("subdomains.txt","r")
# read all content
content = file.read()
# split by new lines
subdomains = content.splitlines()
link = ('admin/','administrator/','wp-login.php','login.php','administration/','admin1/','admin2/','admin3/','admin4/','admin5/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',

'memberadmin/','administratorlogin/','adm/','account.asp','admin/account.asp','admin/index.asp','admin/login.asp','admin/admin.asp','/login.aspx',

'admin_area/admin.asp','admin_area/login.asp','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',

'admin_area/admin.html','admin_area/login.html','admin_area/index.html','admin_area/index.asp','bb-admin/index.asp','bb-admin/login.asp','bb-admin/admin.asp',

'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','admin/controlpanel.html','admin.html','admin/cp.html','cp.html',

'administrator/index.html','administrator/login.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator.html',

'moderator/login.html','moderator/admin.html','account.html','controlpanel.html','admincontrol.html','admin_login.html','panel-administracion/login.html',

'admin/home.asp','admin/controlpanel.asp','admin.asp','pages/admin/admin-login.asp','admin/admin-login.asp','admin-login.asp','admin/cp.asp','cp.asp',

'administrator/account.asp','administrator.asp','acceso.asp','login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','administrator/login.asp',

'moderator/admin.asp','controlpanel.asp','admin/account.html','adminpanel.html','webadmin.html','administration','pages/admin/admin-login.html','admin/admin-login.html',

'webadmin/index.html','webadmin/admin.html','webadmin/login.html','user.asp','user.html','admincp/index.asp','admincp/login.asp','admincp/index.html',

'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','adminarea/index.html','adminarea/admin.html','adminarea/login.html',

'panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admin/admin_login.html',

'admincontrol/login.html','adm/index.html','adm.html','admincontrol.asp','admin/account.asp','adminpanel.asp','webadmin.asp','webadmin/index.asp',

'webadmin/admin.asp','webadmin/login.asp','admin/admin_login.asp','admin_login.asp','panel-administracion/login.asp','adminLogin.asp',

'admin/adminLogin.asp','home.asp','admin.asp','adminarea/index.asp','adminarea/admin.asp','adminarea/login.asp','admin-login.html',

'panel-administracion/index.asp','panel-administracion/admin.asp','modelsearch/index.asp','modelsearch/admin.asp','administrator/index.asp',

'admincontrol/login.asp','adm/admloginuser.asp','admloginuser.asp','admin2.asp','admin2/login.asp','admin2/index.asp','adm/index.asp',

'adm.asp','affiliate.asp','adm_auth.asp','memberadmin.asp','administratorlogin.asp','siteadmin/login.asp','siteadmin/index.asp','siteadmin/login.html','memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',

'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',

'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',

'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',

'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',

'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',

'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',

'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',

'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',

'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html',

'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',

'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',

'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',

'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',

'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',

'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',

'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',

'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php','adm/','admin/account.cfm','admin/index.cfm','admin/login.cfm','admin/admin.cfm','admin/account.cfm',

'admin_area/admin.cfm','admin_area/login.cfm','siteadmin/login.cfm','siteadmin/index.cfm','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',

'admin_area/index.cfm','bb-admin/index.cfm','bb-admin/login.cfm','bb-admin/admin.cfm','admin/home.cfm','admin_area/login.html','admin_area/index.html',

'admin/controlpanel.cfm','admin.cfm','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',

'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',

'admin/cp.cfm','cp.cfm','administrator/index.cfm','administrator/login.cfm','nsw/admin/login.cfm','webadmin/login.cfm','admin/admin_login.cfm','admin_login.cfm',

'administrator/account.cfm','administrator.cfm','admin_area/admin.html','pages/admin/admin-login.cfm','admin/admin-login.cfm','admin-login.cfm',

'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cfm','modelsearch/login.cfm','moderator.cfm','moderator/login.cfm',

'moderator/admin.cfm','account.cfm','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cfm','admincontrol.cfm',

'admin/adminLogin.html','acceso.cfm','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cfm','adminarea/index.html','adminarea/admin.html',

'webadmin.cfm','webadmin/index.cfm','webadmin/admin.cfm','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cfm','moderator.html',

'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',

'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',

'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cfm','account.html','controlpanel.html','admincontrol.html',

'panel-administracion/login.cfm','wp-login.cfm','adminLogin.cfm','admin/adminLogin.cfm','home.cfm','admin.cfm','adminarea/index.cfm',

'adminarea/admin.cfm','adminarea/login.cfm','panel-administracion/index.cfm','panel-administracion/admin.cfm','modelsearch/index.cfm',

'modelsearch/admin.cfm','admincontrol/login.cfm','adm/admloginuser.cfm','admloginuser.cfm','admin2.cfm','admin2/login.cfm','admin2/index.cfm','usuarios/login.cfm',

'adm/index.cfm','adm.cfm','affiliate.cfm','adm_auth.cfm','memberadmin.cfm','administratorlogin.cfm','adminLogin/','admin_area/','panel-administracion/','instadmin/','login.aspx',

'memberadmin/','administratorlogin/','adm/','admin/account.aspx','admin/index.aspx','admin/login.aspx','admin/admin.aspx','admin/account.aspx',

'admin_area/admin.aspx','admin_area/login.aspx','siteadmin/login.aspx','siteadmin/index.aspx','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',

'admin_area/index.aspx','bb-admin/index.aspx','bb-admin/login.aspx','bb-admin/admin.aspx','admin/home.aspx','admin_area/login.html','admin_area/index.html',

'admin/controlpanel.aspx','admin.aspx','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',

'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',

'admin/cp.aspx','cp.aspx','administrator/index.aspx','administrator/login.aspx','nsw/admin/login.aspx','webadmin/login.aspx','admin/admin_login.aspx','admin_login.aspx',

'administrator/account.aspx','administrator.aspx','admin_area/admin.html','pages/admin/admin-login.aspx','admin/admin-login.aspx','admin-login.aspx',

'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.aspx','modelsearch/login.aspx','moderator.aspx','moderator/login.aspx',

'moderator/admin.aspx','acceso.aspx','account.aspx','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.aspx','admincontrol.aspx',

'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.aspx','adminarea/index.html','adminarea/admin.html',

'webadmin.aspx','webadmin/index.aspx','webadmin/admin.aspx','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.aspx','moderator.html',

'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',

'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',

'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.aspx','account.html','controlpanel.html','admincontrol.html',

'panel-administracion/login.aspx','wp-login.aspx','adminLogin.aspx','admin/adminLogin.aspx','home.aspx','admin.aspx','adminarea/index.aspx',

'adminarea/admin.aspx','adminarea/login.aspx','panel-administracion/index.aspx','panel-administracion/admin.aspx','modelsearch/index.aspx',

'modelsearch/admin.aspx','admincontrol/login.aspx','adm/admloginuser.aspx','admloginuser.aspx','admin2.aspx','admin2/login.aspx','admin2/index.aspx','usuarios/login.aspx',

'adm/index.aspx','adm.aspx','affiliate.aspx','adm_auth.aspx','memberadmin.aspx','administratorlogin.aspx','memberadmin/','administratorlogin/','adm/','admin/account.js','admin/index.js','admin/login.js','admin/admin.js','admin/account.js',

'admin_area/admin.js','admin_area/login.js','siteadmin/login.js','siteadmin/index.js','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',

'admin_area/index.js','bb-admin/index.js','bb-admin/login.js','bb-admin/admin.js','admin/home.js','admin_area/login.html','admin_area/index.html',

'admin/controlpanel.js','admin.js','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',

'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',

'admin/cp.js','cp.js','administrator/index.js','administrator/login.js','nsw/admin/login.js','webadmin/login.js','admin/admin_login.js','admin_login.js',

'administrator/account.js','administrator.js','admin_area/admin.html','pages/admin/admin-login.js','admin/admin-login.js','admin-login.js',

'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.js','modelsearch/login.js','moderator.js','moderator/login.js',

'moderator/admin.js','account.js','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.js','admincontrol.js',

'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.js','adminarea/index.html','adminarea/admin.html',

'webadmin.js','webadmin/index.js','acceso.js','webadmin/admin.js','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.js','moderator.html',

'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',

'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',

'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.js','account.html','controlpanel.html','admincontrol.html',

'panel-administracion/login.js','wp-login.js','adminLogin.js','admin/adminLogin.js','home.js','admin.js','adminarea/index.js',

'adminarea/admin.js','adminarea/login.js','panel-administracion/index.js','panel-administracion/admin.js','modelsearch/index.js',

'modelsearch/admin.js','admincontrol/login.js','adm/admloginuser.js','admloginuser.js','admin2.js','admin2/login.js','admin2/index.js','usuarios/login.js',

'adm/index.js','adm.js','affiliate.js','adm_auth.js','memberadmin.js','administratorlogin.js','bb-admin/index.cgi','bb-admin/login.cgi','bb-admin/admin.cgi','admin/home.cgi','admin_area/login.html','admin_area/index.html',

'admin/controlpanel.cgi','admin.cgi','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',

'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',

'admin/cp.cgi','cp.cgi','administrator/index.cgi','administrator/login.cgi','nsw/admin/login.cgi','webadmin/login.cgi','admin/admin_login.cgi','admin_login.cgi',

'administrator/account.cgi','administrator.cgi','admin_area/admin.html','pages/admin/admin-login.cgi','admin/admin-login.cgi','admin-login.cgi',

'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cgi','modelsearch/login.cgi','moderator.cgi','moderator/login.cgi',

'moderator/admin.cgi','account.cgi','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cgi','admincontrol.cgi',

'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cgi','adminarea/index.html','adminarea/admin.html',

'webadmin.cgi','webadmin/index.cgi','acceso.cgi','webadmin/admin.cgi','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cgi','moderator.html',

'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',

'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',

'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cgi','account.html','controlpanel.html','admincontrol.html',

'panel-administracion/login.cgi','wp-login.cgi','adminLogin.cgi','admin/adminLogin.cgi','home.cgi','admin.cgi','adminarea/index.cgi',

'adminarea/admin.cgi','adminarea/login.cgi','panel-administracion/index.cgi','panel-administracion/admin.cgi','modelsearch/index.cgi',

'modelsearch/admin.cgi','admincontrol/login.cgi','adm/admloginuser.cgi','admloginuser.cgi','admin2.cgi','admin2/login.cgi','admin2/index.cgi','usuarios/login.cgi',

'adm/index.cgi','adm.cgi','affiliate.cgi','adm_auth.cgi','memberadmin.cgi','administratorlogin.cgi','admin_area/admin.brf','admin_area/login.brf','siteadmin/login.brf','siteadmin/index.brf','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',

'admin_area/index.brf','bb-admin/index.brf','bb-admin/login.brf','bb-admin/admin.brf','admin/home.brf','admin_area/login.html','admin_area/index.html',

'admin/controlpanel.brf','admin.brf','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',

'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',

'admin/cp.brf','cp.brf','administrator/index.brf','administrator/login.brf','nsw/admin/login.brf','webadmin/login.brfbrf','admin/admin_login.brf','admin_login.brf',

'administrator/account.brf','administrator.brf','acceso.brf','admin_area/admin.html','pages/admin/admin-login.brf','admin/admin-login.brf','admin-login.brf',

'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.brf','modelsearch/login.brf','moderator.brf','moderator/login.brf',

'moderator/admin.brf','account.brf','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.brf','admincontrol.brf',

'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.brf','adminarea/index.html','adminarea/admin.html',

'webadmin.brf','webadmin/index.brf','webadmin/admin.brf','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.brf','moderator.html',

'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',

'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',

'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.brf','account.html','controlpanel.html','admincontrol.html',

'panel-administracion/login.brf','wp-login.brf','adminLogin.brf','admin/adminLogin.brf','home.brf','admin.brf','adminarea/index.brf',

'adminarea/admin.brf','adminarea/login.brf','panel-administracion/index.brf','panel-administracion/admin.brf','modelsearch/index.brf',

'modelsearch/admin.brf','admincontrol/login.brf','adm/admloginuser.brf','admloginuser.brf','admin2.brf','admin2/login.brf','admin2/index.brf','usuarios/login.brf',

'admindex.brf','adm.brf','affiliate.brf','adm_auth.brf','memberadmin.brf','administratorlogin.brf','cpanel','cpanel.php','cpanel.html','cpanel.html','admin','administrator','admin1','adm_cp','admin_panel.html','admin_panel','administratorlogin.cgi','memberadmin.cgi','adm_auth.cgi','affiliate.cgi','adm.cgi','adm/index.cgi','usuarios/login.cgi','admin2/index.cgi','admin2/login.cgi','admin2.cgi','admloginuser.cgi','adm/admloginuser.cgi','admincontrol/login.cgi','modelsearch/admin.cgi','modelsearch/index.cgi','panel-administracion/admin.cgi','panel-administracion/index.cgi','adminarea/login.cgi','adminarea/admin.cgi','adminarea/index.cgi','home.cgi','admin/adminLogin.cgi','adminLogin.cgi','wp-login.cgi','panel-administracion/login.cgi','user.cgi','adminpanel.cgi','webadmin/admin.cgi','acceso.cgi','webadmin/index.cgi','webadmin.cgi','rcjakar/admin/login.cgi','admincontrol.cgi','controlpanel.cgi','account.cgi','moderator/admin.cgi','moderator/login.cgi','moderator.cgi','modelsearch/login.cgi','login.cgi','admin-login.cgi','admin/admin-login.cgi','pages/admin/admin-login.cgi','administrator.cgi','administrator/account.cgi','admin_login.cgi','admin/admin_login.cgi','webadmin/login.cgi','nsw/admin/login.cgi','administrator/login.cgi','administrator/index.cgi','cp.cgi','admin/cp.cgi','admin.cgi','admin/controlpanel.cgi','admin/home.cgi','bb-admin/admin.cgi','bb-admin/login.cgi','bb-admin/index.cgi','bb-admin/index.cgi','admin_area/index.cgi','siteadmin/index.cgi','siteadmin/login.cgi','admin_area/login.cgi','admin2','admin3','admin4','admin5','usuarios','usuario','moderator','webadmin','adminarea','bb-admin','adminLogin','admin_area','panel-administracion','instadmin','memberadmin','administratorlogin','adm','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html','admin_area/index.php','bb-admin/index.php','bb-admin/login.php','admin/home.php','bb-admin/admin.php','admin_area/login.html','admin/controlpanel.php','admin_area/index.html','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','adminpanel.html','webadmin.html','webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html','admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php','administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php','bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php','moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php','admin/adminLogin.html','adminLogin.html','rcjakar/admin/login.php','home.html','adminarea/index.html','adminarea/admin.html','webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html','administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html','panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','adminarea/index.php','adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php','modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php','adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php','account.asp','admin/account.asp','admin/index.asp','admin/login.asp','admin/admin.asp','admin_area/admin.asp','admin_area/login.asp','admin_area/index.asp','bb-admin/index.asp','bb-admin/login.asp','bb-admin/admin.asp','admin/home.asp','admin/controlpanel.asp','admin.asp','pages/admin/admin-login.asp','admin/admin-login.asp','admin-login.asp','admin/cp.asp','cp.asp','administrator/account.asp','administrator.asp','acceso.asp','login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','administrator/login.asp','moderator/admin.asp','controlpanel.asp','user.asp','admincontrol.asp','adminpanel.asp','webadmin.asp','webadmin/index.asp','webadmin/admin.asp','webadmin/login.asp','admin/admin_login.asp','admin_login.asp','panel-administracion/login.asp','adminLogin.asp','admin/adminLogin.asp','home.asp','adminarea/index.asp','adminarea/admin.asp','adminarea/login.asp','panel-administracion/index.asp','panel-administracion/admin.asp','modelsearch/index.asp','modelsearch/admin.asp','administrator/index.asp','admincontrol/login.asp','adm/admloginuser.asp','admloginuser.asp','admin2.asp','admin2/login.asp','admin2/index.asp','adm/index.asp','adm.asp','affiliate.asp','adm_auth.asp','memberadmin.asp','administratorlogin.asp','siteadmin/login.asp','siteadmin/index.asp','admin/account.cfm','admin/index.cfm','admin/login.cfm','admin/admin.cfm','admin_area/admin.cfm','admin_area/login.cfm','siteadmin/login.cfm','siteadmin/index.cfm','admin_area/index.cfm','bb-admin/index.cfm','bb-admin/login.cfm','bb-admin/admin.cfm','admin/home.cfm','admin/controlpanel.cfm','admin.cfm','admin/cp.cfm','cp.cfm','administrator/index.cfm','administrator/login.cfm','nsw/admin/login.cfm','webadmin/login.cfm','admin/admin_login.cfm','admin_login.cfm','administrator/account.cfm','administrator.cfm','pages/admin/admin-login.cfm','admin/admin-login.cfm','admin-login.cfm','login.cfm','modelsearch/login.cfm','moderator.cfm','moderator/login.cfm','moderator/admin.cfm','account.cfm','controlpanel.cfm','admincontrol.cfm','acceso.cfm','rcjakar/admin/login.cfm','webadmin.cfm','webadmin/index.cfm','webadmin/admin.cfm','adminpanel.cfm','user.cfm','panel-administracion/login.cfm','wp-login.cfm','adminLogin.cfm','admin/adminLogin.cfm','home.cfm','adminarea/index.cfm','adminarea/admin.cfm','adminarea/login.cfm','panel-administracion/index.cfm','panel-administracion/admin.cfm','modelsearch/index.cfm','modelsearch/admin.cfm','admincontrol/login.cfm','adm/admloginuser.cfm','admin2.cfm','admin2/login.cfm','admin2/index.cfm','usuarios/login.cfm','adm/index.cfm','adm.cfm','affiliate.cfm','adm_auth.cfm','memberadmin.cfm','administratorlogin.cfm','admin/account.js','admin/index.js','admin/login.js','admin/admin.js','admin_area/admin.js','admin_area/login.js','siteadmin/login.js','siteadmin/index.js','admin_area/index.js','bb-admin/index.js','bb-admin/login.js','bb-admin/admin.js','admin/home.js','admin/controlpanel.js','admin.js','admin/cp.js','cp.js','administrator/index.js','administrator/login.js','nsw/admin/login.js','webadmin/login.js','admin/admin_login.js','admin_login.js','administrator/account.js','administrator.js','pages/admin/admin-login.js','admin/admin-login.js','admin-login.js','login.js','modelsearch/login.js','moderator.js','moderator/login.js','moderator/admin.js','account.js','controlpanel.js','admincontrol.js','rcjakar/admin/login.js','webadmin.js','webadmin/index.js','acceso.js','webadmin/admin.js','adminpanel.js','user.js','panel-administracion/login.js','wp-login.js','adminLogin.js','admin/adminLogin.js','home.js','adminarea/index.js','adminarea/admin.js','adminarea/login.js','panel-administracion/index.js','panel-administracion/admin.js','modelsearch/index.js','modelsearch/admin.js','admincontrol/login.js','adm/admloginuser.js','admloginuser.js','admin2.js','admin2/login.js','admin2/index.js','usuarios/login.js','adm/index.js','adm.js','affiliate.js','adm_auth.js','memberadmin.js','administratorlogin.js','admin/account.cgi','admin/index.cgi','admin/login.cgi','admin/admin.cgi',)

def clear():
  
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')

if mainName == '                     Created by Kaveesha Anuhas':
    ascii_banner = pyfiglet.figlet_format("Welcome To WebHunter")
    print(bcolors.MAIN+ascii_banner)
    print(bcolors.WARNING+mainName)
    print(bcolors.FAIL+"A Powerfull Website Scanner")
    print(" ")
    print(bcolors.MAIN1+"Enter your name")
    print("          ")
    username = input("WebScanBot@Admin:>")
    clear()
    ascii_banner = pyfiglet.figlet_format("Hello "+username+"!")
    print(bcolors.MAIN+ascii_banner)
    print(bcolors.FAIL+"A Powerfull Website Scanner")
    print(" ")
    print("Enter Website Link Without WWW & HTTP,HTTPS ")
    print(" ")
    webLink = input("Enter Website Link :>")
    clear()
    ascii_banner = pyfiglet.figlet_format("Welcome To WebScanBot")
    print(bcolors.MAIN+ascii_banner)
    print(bcolors.WARNING+mainName)
    print(bcolors.FAIL+"A Powerfull Website Scanner")
    url = "http://www.kite.com"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        print(bcolors.ENDC+"Connected to the Internet")
    except (requests.ConnectionError, requests.Timeout) as exception:
        print(bcolors.FAIL+"No internet connection.")
    print(bcolors.MAIN1+"Website Link --> "+webLink)
    print("  ")
    print("  ")
    print(bcolors.WARNING+"1. Scan Web IP Address Status")
    print(bcolors.WARNING+"2. Scan Web TCP Open Ports")
    print(bcolors.WARNING+"3. Scan Web Admin Link")
    print(bcolors.WARNING+"4. Scan Web Subdomains")
    print(bcolors.WARNING+"5. Scan Web Domain Name of a Host")
    print(bcolors.WARNING+"6. Ping Website")
    print(bcolors.WARNING+"7. Scan Website And Analytics Full Data")
    print(bcolors.WARNING+"8. Scan Website Host Server Location")

    print(" ")
    as2ga3 = input("WebScanBot@"+username+":>")
    if as2ga3 == "1. Scan Web Ip" or as2ga3 == "1." or as2ga3 == "1":
        ascii_banner = pyfiglet.figlet_format("Welcome To WebScanBot")
        print(bcolors.MAIN+ascii_banner)
        print(bcolors.WARNING+mainName)
        print(bcolors.FAIL+"A Powerfull Website Scanner")
        ip = s.gethostbyname(webLink)
        ipLoc = geocoder.ip(ip)
        print("  ")
        print(webLink+" Ip --> "+ip)
    elif as2ga3 == "3. Scan Web Admin Link" or as2ga3 == "3." or as2ga3 == "3":
        clear()
        ascii_banner = pyfiglet.figlet_format("Welcome To WebScanBot")
        print(bcolors.MAIN+ascii_banner)
        print(bcolors.WARNING+mainName)
        print(bcolors.FAIL+"A Powerfull Website Scanner")
        print(" ")
        print(" ")
        awebaLink = f"http://www.{webLink}"
        for link2 in link :
            link3 = awebaLink+"/"+link2
            try :
                openurl = urllib.request.urlopen(link3)
                print("\n\033[1;34m" + "ADMIN PAGE ITS FOUND : "+link3)
            except urllib.error.URLError as msg :
                print ("\n\033[33;39mADMIN PAGE NOT FOUND : "+link3)
    elif as2ga3 == "2. Scan Web Open Ports" or as2ga3 == "2." or as2ga3 == "2":
        clear()
        ascii_banner = pyfiglet.figlet_format("Welcome To WebScanBot")
        print(bcolors.MAIN+ascii_banner)
        print(bcolors.WARNING+mainName)
        print(bcolors.FAIL+"A Powerfull Website Scanner")
        ip = s.gethostbyname(webLink)
        print("  ")
        print("-" * 50)
        print(bcolors.FAIL+webLink+" IP Address --> "+ip)
        print(bcolors.FAIL+"Scanning started at:" + str(datetime.now()))
        print(bcolors.FAIL+"Some Website will take some time")
        print("-" * 50)
        print(" ")
        try:
            for port in range(1,65535):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = s.connect_ex((ip,port))
                if result ==0:
                    print(bcolors.WARNING+"Port {} is open".format(port))
                    s.close()
                else:
                    print(bcolors.FAIL+"Port {} is Close".format(port))
                    s.close()
        except KeyboardInterrupt:
            print("\n Exiting Program !!!!")
            sys.exit()
        except socket.gaierror:
            print("\n Hostname Could Not Be Resolved !!!!")
            sys.exit()
        except socket.error:
            print("\ Server not responding !!!!")
            sys.exit()
    elif as2ga3 == "4. Scan Web Subdomains" or as2ga3 == "4." or as2ga3 == "4":
        clear()
        ascii_banner = pyfiglet.figlet_format("Welcome To WebScanBot")
        print(bcolors.MAIN+ascii_banner)
        print(bcolors.WARNING+mainName)
        print(bcolors.FAIL+"A Powerfull Website Scanner")
        ip = s.gethostbyname(webLink)
        print("  ")
        print("-" * 50)
        print(bcolors.FAIL+webLink+" IP Address --> "+ip)
        print(bcolors.FAIL+"Scanning started at:" + str(datetime.now()))
        print(bcolors.FAIL+"This will take some time")
        print("-" * 50)
        print(" ")
        discovered_subdomains = []
        for subdomain in subdomains:
            url = f"http://{subdomain}.{webLink}"
            try:
                requests.get(url)
            except requests.ConnectionError:
                pass
            else:
                print(bcolors.MAIN1+"[+] Found subdomain:", url)
                discovered_subdomains.append(url)
    elif as2ga3 == "5. Scan Web Domain Name of a Host" or as2ga3 == "5." or as2ga3 == "5":
        clear()
        ascii_banner = pyfiglet.figlet_format("Welcome To WebScanBot")
        print(bcolors.MAIN+ascii_banner)
        print(bcolors.WARNING+mainName)
        print(bcolors.FAIL+"A Powerfull Website Scanner")
        ip = s.gethostbyname(webLink)
        print("  ")
        print("-" * 50)
        print(bcolors.FAIL+webLink+" IP Address --> "+ip)
        print(bcolors.FAIL+"Scanning started at:" + str(datetime.now()))
        print(bcolors.FAIL+"This will take some time")
        print("-" * 50)
        print(" ")
        whois_info = whois.whois(webLink)
        print(bcolors.WARNING+"Domain registrar:", whois_info.registrar)
        print(bcolors.WARNING+"WHOIS server:", whois_info.whois_server)
        print(bcolors.WARNING+"Domain creation date:", whois_info.creation_date)
        print(bcolors.WARNING+"Expiration date:", whois_info.expiration_date)

    elif as2ga3 == "6. Ping Website" or as2ga3 == "6." or as2ga3 == "6":
        clear()
        ascii_banner = pyfiglet.figlet_format("Welcome To WebScanBot")
        print(bcolors.MAIN+ascii_banner)
        print(bcolors.WARNING+mainName)
        print(bcolors.FAIL+"A Powerfull Website Scanner")
        ip = s.gethostbyname(webLink)
        print("  ")
        print("-" * 50)
        print(bcolors.FAIL+webLink+" IP Address --> "+ip)
        print(bcolors.FAIL+"Scanning started at:" + str(datetime.now()))
        print(bcolors.FAIL+"This will take some time")
        print("-" * 50)
        print(" ")
        packet = int(input("\nEnter Packet: "))
        print("\n")
        ping = subprocess.getoutput(f"ping -w {packet} {webLink}")
        print(bcolors.WARNING+ping)

    elif as2ga3 == "7. Scan Website And Analytics Full Data" or as2ga3 == "7." or as2ga3 == "7":
        clear()
        ascii_banner = pyfiglet.figlet_format("Welcome To WebScanBot")
        print(bcolors.MAIN+ascii_banner)
        print(bcolors.WARNING+mainName)
        print(bcolors.FAIL+"A Powerfull Website Scanner")
        ip = s.gethostbyname(webLink)
        print("  ")
        print("-" * 50)
        print(bcolors.FAIL+webLink+" IP Address --> "+ip)
        print(bcolors.FAIL+"Scanning started at:" + str(datetime.now()))
        print(bcolors.FAIL+"This will take some time")
        print("-" * 50)
        print(" ")
        url = f"http://{webLink}.com"
        result = urllib.request.urlopen('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={}/&strategy=mobile'\
            .format(url)).read().decode('UTF-8')
        print(result)

    elif as2ga3 == "8. Scan Website Host Server Location" or as2ga3 == "8." or as2ga3 == "8":
        clear()
        ascii_banner = pyfiglet.figlet_format("Welcome To WebScanBot")
        print(bcolors.MAIN+ascii_banner)
        print(bcolors.WARNING+mainName)
        print(bcolors.FAIL+"A Powerfull Website Scanner")
        ip = s.gethostbyname(webLink)
        print("  ")
        print("-" * 50)
        response = requests.post("http://ip-api.com/json/"+ip).json()
        print("Server IP --> "+ip+"\n"+" "+"\n"+"Server Location"+"\n"+"-------------------------"+"\n"+"📌Country --> "+response["country"]+"\n"+"📌CountryCode --> "+response["countryCode"]+"\n"+"📌Region --> "+response["region"]+"\n"+"📌RegionName --> "+response["regionName"]+"\n"+"📌City --> "+response["city"]+"\n"+"📌Zip --> "+response["zip"]+"\n"+"-------------------------"+"\n"+"📌Isp --> "+response["isp"]+"\n"+"📌Org --> "+response["org"]+"\n"+"📌As --> "+response["as"]+"\n"+"📌Latitude --> "+str(response["lat"])+"\n"+"📌Longtitude --> "+str(response["lon"]))
        


    else:
        pass
else:
    clear()
    ascii_banner = pyfiglet.figlet_format("Error")
    print(bcolors.MAIN+ascii_banner)
    print('You Cant Edit Alienbot Code')
