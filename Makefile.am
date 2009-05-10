## Process this file with automake to produce Makefile.in

SUBDIRS = src tools examples doc test debian

pkgconfigdir = $(libdir)/pkgconfig
pkgconfig_DATA = gts.pc

ChangeLog:
	darcs changes > ChangeLog

debian-snapshot: config.h
	darcs changes > ChangeLog
	sh debian/changelog.sh
	dpkg-buildpackage -rfakeroot -b
	rm -f debian/repo/*
	mv -f ../*.changes ../*.deb debian/repo
	cd debian/repo && dpkg-scanpackages . /dev/null | gzip -9c > Packages.gz

launchpad-snapshot: config.h dist
	tar xzf gts-?.?.?.tar.gz
	cd gts-?.?.? && ./configure && darcs changes > ChangeLog && sh debian/changelog.sh && dpkg-buildpackage -rfakeroot -k07AB22DC -S -sa
	rm -f gts-?.?.?.tar.gz
	rm -r -f gts-?.?.?
