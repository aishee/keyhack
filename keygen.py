#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import base64
import requests

print "- Script generator invite code for Hackthebox"
print "- Please wait one moment...."
bs64request = requests.post(
    "https://www.Hackthebox.eu/api/invite/generate", json={
        "key": "value"
    }).json()["data"]["code"]
print "- Invite code: ", base64.b64decode(bs64request)
print "- Thanks you! BreakTeam - Anounys"
