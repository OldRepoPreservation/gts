## Process this file with automake to produce Makefile.in

SUBDIRS = src tools examples doc test

pkgconfigdir = $(libdir)/pkgconfig
pkgconfig_DATA = gts.pc

changelog:
	darcs changes > ChangeLog
