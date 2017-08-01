# ApkInfoExtractor
This Program will extract important information from AndroidManifest.xml file into .csv file

You will get Package Name, Launch Activity Name, Permissions, all activity names and All the services.

<h2>Usage:</h2>
<p>
<code>
./ApkInfoExtractor.sh <i>YourApk</i>.apk
</code>
</p>


<p>Output will be stored in <i>apkname</i>.csv file.</p>




<p>Edit "ApkInforExtractor.sh" file to process multiple apk's at once.</p>



<h2>Note :</h2>

This code is based on <b>aapt</b> ouput

<b>aapt</b> is a part of android sdk tools.

Install Android SDK tools if aapt command fails.
