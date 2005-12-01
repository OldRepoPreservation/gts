version=`awk '{if ($1 == "Version:") print $2;}' < gts.pc`
date=`date "+%a, %e %b %Y %T %z"`

cat <<EOF > debian/changelog
gts-snapshot ($version) testing; urgency=low

  * gts-snapshot release (based on Marcelo's official debian)

 -- Stephane Popinet <popinet@users.sf.net>  $date
EOF
