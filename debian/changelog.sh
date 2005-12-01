
date=`date "+%a, %e %b %Y %T %z"`
version=`date "+%y.%m.%d"`

cat <<EOF > debian/changelog
gts-snapshot ($version) testing; urgency=low

  * gts-snapshot release (based on Marcelo's official debian)

 -- Stephane Popinet <popinet@users.sf.net>  $date
EOF
