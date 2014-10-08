# -*- coding: utf-8 -*-

srvc_name = 'bnw.test'
srvc_pwd = 'test'
xmpp_server = '127.0.0.1:9781'
admin_jid = 'admin@localhost'
database_uri = 'mongodb://127.0.0.1/bnw_test'
database_rs = ''
database = 'bnw_test'
database_fs = 'bnw_test_fs'
webui_enabled = True
webui_port = 9782
webui_base = 'localhost:9782'
webui_wsbase = 'localhost:9782'
webui_static = 'localhost:9782'
search_db = '/tmp/bnw_xapian'
search_language = 'english'
search_port = 9783
rpc_enabled = False
rpc_port = 8081
blob_storage = 'http://127.0.0.1:9784/'
manhole = ''
trace_shutdown = False
throttle_leak_speed = 5 # seconds
throttle_bucket_size = 5 << 20 # number of actions
mapreduce_enabled = True
thumbor = 'http://127.0.0.1:9785'
thumbor_key = 'ABCDEF'
thumbor_pars = { 'width': 256, 'height': 256, 'fit_in': True }
statd = '127.0.0.1:8125'
