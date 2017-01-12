!#/usr/bin bash
for filename in *
do
    echo "$filename"
    head -2 $filename
    echo ""
done
