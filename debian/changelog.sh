GTS_VERSION=`pkg-config gts --modversion`

version=`date +%y%m%d`
date=`date +"%a, %e %b %Y %T %z"`
cat <<EOF > debian/changelog
gts-snapshot ($GTS_VERSION-$version) testing; urgency=low

  * gts-snapshot release (based on Marcelo's official debian)

 -- Stephane Popinet <popinet@users.sf.net>  $date
EOF
