[app]
title = Barcode Scanner
package.name = barcodescanner
package.domain = com.yourcompany
source.dir = .
version = 0.1
requirements = python3,kivy,kivymd,pyzbar,pillow
orientation = portrait
android.permissions = CAMERA
entrypoint = main.py
source.include_exts = py,png,jpg,kv,atlas
android.ndk = 25c
android.api = 31
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
logcat = true
copy_libs = 1
build_no = 1
