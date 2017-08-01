import re
import sys
import csv
import os
from subprocess import call

with open(sys.argv[1]) as f:
	text=f.readlines();

#CSV files

splittext = os.path.splitext(os.path.splitext(sys.argv[1])[0])[0]
print splittext
fcsv= open(splittext+".csv", 'wt')
fpackage = csv.writer(fcsv)




launchfound=False
for record in text:
	matchpackage = re.search("package: name",record)
	if matchpackage: #package: name='com.melodis.midomiMusicIdentifier.freemium' versionCode='20040' versionName='7.6.0' platformBuildVersionName='7.1.1'
		match= re.search(r'(package: name=\')([^\']*)(\.*)',record)


		#print "package name is : "+ match.group(2) #prints package name
		fpackage.writerow(("Package_Name",match.group(2)))
		package_name=match.group(2)
		#print record


	matchlaunch = re.search("launchable-activity:",record)
	#launchable-activity: name='com.soundhound.android.appcommon.activity.SplashScreenActivity'  label='SoundHound' icon=''
	if matchlaunch:
		launchfound= True
		matchl=re.search(r'(launchable-activity: name=\')([^\']*)(\.*)',record)
		matchlab=re.search(r'.*?(label=\')([^\']*)(\.*)',record)
		
		#print "launch activity is : " + matchl.group(2) #prints launch activity
		fpackage.writerow(("Launch_Activity",match.group(2)))
		##print "label is : " + matchlab.group(2)  #prints label activity
		launch_activity=matchl.group(2)
		#print record
if launchfound:
	pass
else:
	with open(sys.argv[2]) as f2:
		xmltextrev= f2.readlines();
	xmltextalias=reversed(xmltextrev)
	iter1=xmltextalias.__iter__()
	i1=0
	length1 = len(xmltextrev)
	while True:
		if i1>=length1:
			break
		try:
			records1 = iter1.next()
		except :
			quit()
		i1=i1+1
		matchaluancher= re.search("android.intent.category.LAUNCHER",records1)
		if matchaluancher:
			while True:
				try:
					records1 = iter1.next()
				except :
					quit()
				i1=i1+1			
				matchtargetact= re.search("A: android:targetActivity",records1)
				if matchtargetact:
					foundact=re.search(r'(A: android:targetActivity)(.*?)(=")(.*?)(")(.*)',records1)
					launch_activity=foundact.group(4)
					#print "launchActivity is :" + foundact.group(4)	
					fpackage.writerow(("Launch_Activity",foundact.group(4)))
					break				


args=(package_name,launch_activity)



for record in text:
	matchpermission = re.search("uses-permission:",record)
	#uses-permission: name='com.melodis.midomiMusicIdentifier.freemium.permission.C2D_MESSAGE'
	if matchpermission:
		matchp=re.search(r'(uses-permission: name=\')([^\']*)(\.*)',record)
		argspermission=(matchp.group(2),package_name)


		
		#print "permission : " +  matchp.group(2)
		fpackage.writerow(("Permission",matchp.group(2)))




'''
      E: activity (line=645)
        A: android:theme(0x01010000)=@0x1030010
        A: android:name(0x01010003)="com.millennialmedia.android.MMAdViewOverlayActivity" (Raw: "com.millennialmedia.android.MMAdViewOverlayActivity")
'''

with open(sys.argv[2]) as f1:
	xmltext= f1.readlines();

iter=xmltext.__iter__()
i=0;
length = len(xmltext)
#print length


while True:
	#print i
	if i>=length:
		break
	try:
		records = iter.next()
	except :
		quit()
	
	i=i+1
	matchact = re.search("E: activity",records)
	if matchact:
		while True:
			try:
				records = iter.next()
			except :
				quit()
			i=i+1
			next1 = re.search("A: android:name",records)
			if next1:
				foundact=re.search(r'(A: android:name)(.*?)(=")(.*?)(")(.*)',records)
				#print "Activity name : "+foundact.group(4)
				fpackage.writerow(("Activity",foundact.group(4)))
				#target.write(foundact.group(4)+"\n")

				break
	matchactserv = re.search("E: service",records)
	if matchactserv:
		while True:
			try:
				records = iter.next()
			except :
				quit()
			i=i+1
			next1 = re.search("A: android:name",records)
			if next1:
				foundact1=re.search(r'(A: android:name)(.*?)(=")(.*?)(")(.*)',records)
				#print "Service name : "+foundact1.group(4)
				fpackage.writerow(("Service",foundact1.group(4)))
				#targetservice.write(foundact1.group(4)+"\n")
				break




