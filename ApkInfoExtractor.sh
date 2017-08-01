
#for entry in ./*.apk
#do
#	echo "######################################################################"
#	echo $entry
#	aapt d badging "$entry" > "$entry"badging.txt
#	aapt dump xmltree "$entry" AndroidManifest.xml > "$entry"xmltree.txt
#	python aapt.py "$entry"badging.txt "$entry"xmltree.txt #> "$entry"result.txt
#	rm "$entry"badging.txt
#	rm "$entry"xmltree.txt
	#rm "$entry"result.txt
#	echo "######################################################################"
#done


aapt d badging "$1" > "$1"badging.txt
aapt dump xmltree "$1" AndroidManifest.xml > "$1"xmltree.txt
python apkinfoextractor.py "$1"badging.txt "$1"xmltree.txt #> "$entry"result.txt
rm "$1"badging.txt
rm "$1"xmltree.txt
