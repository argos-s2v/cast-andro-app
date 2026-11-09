[app]
title = CAST OPS
package.name = castops
package.domain = org.castops
source.dir = .
source.include_exts = py,png
version = 1.1
requirements = python3,kivy==2.3.0,openssl,requests,urllib3,chardet,idna,certifi,casttube,yt-dlp
orientation = portrait
fullscreen = 0
icon.filename = %(source.dir)s/icon.png
android.presplash_color = #050805
android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE
android.api = 33
android.minapi = 24
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
