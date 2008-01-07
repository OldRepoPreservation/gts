%define alphatag %(date +%Y%m%d)
%define current %(gts-config --version)

Summary: GNU Triangulated Surface Library
Name: gts-snapshot
%if "%{current}" == ""
Version: 0.7.6
%else
Version: %{current}
%endif
Release: 4.%{alphatag}cvs%{?dist}
License: GPLv2
Group: Applications/Engineering
URL: http://gts.sourceforge.net
Packager: Ivan Adam Vari <i.vari@niwa.co.nz>
Source0: gts-mainline.tar.gz
Provides: %{name}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: glib2-devel
%if 0%{?fedora_version}
BuildRequires: netpbm-devel
%elif 0%{?suse_version}
BuildRequires: libnetpbm
%endif

%package devel
Summary:        Development files for gts
Group:          Applications/Engineering
Requires:       glib2-devel pkgconfig
Requires:       %{name} = %{version}-%{release}

%description
GTS provides a set of useful functions to deal with 3D surfaces meshed
with interconnected triangles including collision detection,
multiresolution models, constrained Delaunay triangulations and robust
set operations (union, intersection, differences).

%description devel
This package contains the gts header files and libs.


%prep
%setup -q -n gts-mainline


%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -fPIC -DPIC"
if [ -x ./configure ]; then
    CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=%{_prefix} \
		--disable-dependency-tracking \
		    --libdir=%{_prefix}/%_lib
else
    CFLAGS="$RPM_OPT_FLAGS" sh autogen.sh \
	--prefix=%{_prefix} \
		--disable-dependency-tracking \
		    --libdir=%{_prefix}/%_lib
fi

%{__make}


%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Fedora compatible changes, won't hurt SuSE
mv -f $RPM_BUILD_ROOT%{_bindir}/delaunay $RPM_BUILD_ROOT%{_bindir}/gtsdelaunay 
mv -f $RPM_BUILD_ROOT%{_bindir}/happrox $RPM_BUILD_ROOT%{_bindir}/gtshapprox
mv -f $RPM_BUILD_ROOT%{_bindir}/transform $RPM_BUILD_ROOT%{_bindir}/gtstransform


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc COPYING NEWS README TODO
%{_bindir}/gtsdelaunay
%{_bindir}/gts2dxf
%{_bindir}/gts2oogl
%{_bindir}/gts2stl
%{_bindir}/gtscheck
%{_bindir}/gtscompare
%{_bindir}/gtstemplate
%{_bindir}/gtshapprox
%{_bindir}/stl2gts
%{_bindir}/gtstransform
%{_libdir}/*.so.*


%files devel
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/gts-config
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4


%changelog
* Mon Jan 7 2008 Ivan Adam Vari <i.vari@niwa.co.nz> - 4
- Removed %{?_smp_mflags} from make due to intermittent
  build errors on some SMP systems

* Wed Dec 19 2007 Ivan Adam Vari <i.vari@niwa.co.nz> - 3
- Fixed creating RPM_BUILD_ROOT issue on some systems
- Fixed package (install) dependencies

* Fri Sep 28 2007 Ivan Adam Vari <i.vari@niwa.co.nz> - 2
- Added SLEx/SuSE compatibility
- Added 64bit compatibility
- Removed --disable-static flag

* Tue May 1 2007 Ivan Adam Vari <i.vari@niwa.co.nz> - 1
- Initial rpm release based on Fedora/Redhat Linux
