[app]
# (str) Title of your application
title = Barcode Scanner

# (str) Package name
package.name = barcodescanner

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py is located
source.dir = .

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy,kivymd,pyzbar,pillow

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = CAMERA

# (str) The entry point for your application
entrypoint = main.py

# (list) Include specific files into the application
source.include_exts = py,png,jpg,kv,atlas

# (str) Android NDK version to use
android.ndk = 25c

# (int) Android SDK version to use
android.api = 31

# (int) Minimum API level for Android
android.minapi = 21

# (list) Supported architectures
android.archs = arm64-v8a

# (bool) Enable logcat when in debug mode
logcat = true

# (bool) Copy libraries inside the APK to use them internally (good for testing)
copy_libs = 1

# (str) The build number
build_no = 1

