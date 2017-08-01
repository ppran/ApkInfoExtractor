# ApkInfoExtractor
This Program will extract important information from AndroidManifest.xml file into .csv file

You will get Package Name, Launch Activity Name, Permissions, all activity names and All the services.

<blockquote>
How to Use:

./ApkInfoExtractor.sh <i>YourApk</i>.apk

Output will be stored in <i>apkname</i>.csv file.
</blockquote>




Edit "ApkInforExtractor.sh" file to process multiple apk's at once.


<blockquote>
Note :

This code is based on "aapt" ouput

aapt is a part of android sdk tools.

Install Android SDk tools if aapt command fails.
</blockquote>
