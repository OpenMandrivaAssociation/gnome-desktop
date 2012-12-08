%define api_version 2
%define lib_major   17
%define libname %mklibname %{name}-%{api_version}_ %{lib_major}
%define develname %mklibname -d %{name}-%{api_version}

Summary:	Package containing code shared among gnome-panel, gnome-session, nautilus, etc
Name:		gnome-desktop
Version:	2.32.1
Release:	8
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/GNOME
URL:		http://www.gnome.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-desktop/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	libxslt-proc
BuildRequires:	intltool >= 0.40.0
BuildRequires:	ldetect-lst

Provides:	%{name}-%{api_version} = %{version}-%{release}
Requires:	ldetect-lst >= 0.1.282
%rename %{name}-common

%description
This package contains some data files and other shared components of the
GNOME user environment.

%package -n %{libname}
Summary:	%{summary}
Group:		System/Libraries

%description -n %{libname}
This package contains an internal library
(libgnomedesktop) used to implement some portions of the GNOME
desktop.

%package -n %{develname}
Summary:	Development libraries, include files for gnome-desktop
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-%{api_version}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{mklibname -d gnome-desktop-2_ 2} < 2.32.1-8

%description -n %{develname}
Development libraries, include files for internal library libgnomedesktop.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static \
	--with-gnome-distributor="%{vendor}" \
	--disable-scrollkeeper \
	--with-pnp-ids-path=%{_datadir}/misc/pnp.ids

%make LIBS=-lm

%install
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std

%find_lang %{name}-2.0

for d in `ls -1 %{buildroot}%{_datadir}/gnome/help/`; do
  %find_lang $d --with-gnome
  cat $d.lang >> %{name}-2.0.lang
done

%files -f %{name}-2.0.lang
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/*
%{_datadir}/gnome-about
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libgnome-desktop-%{api_version}.so.%{lib_major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%doc %{_datadir}/gtk-doc/html/*



%changelog
* Thu Feb 23 2012 Jon Dill <dillj@mandriva.org> 2.32.1-7
+ Revision: 779421
- rebuild against new version of libffi4

* Wed Nov 23 2011 Matthew Dawkins <mattydaw@mandriva.org> 2.32.1-6
+ Revision: 732793
- rebuild
- major spec clean up
- removed defattr
- removed .la files
- disabled static build
- removed old ldconfig scripts
- removed unneed scrollkeeper, scriptlets, BR etc
- merged common pkg (locales) into main pkg
- removed unnecessary requires in lib & devel pkg
- fixed devel summary & description
- removed mkrel & BuildRoot

* Mon Oct 24 2011 GÃ¶tz Waschk <waschk@mandriva.org> 2.32.1-5
+ Revision: 705823
- rebuild for new xcb

* Wed Sep 28 2011 GÃ¶tz Waschk <waschk@mandriva.org> 2.32.1-4
+ Revision: 701694
- rebuild for new libpng

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.32.1-3
+ Revision: 664862
- mass rebuild

* Mon Feb 07 2011 Funda Wang <fwang@mandriva.org> 2.32.1-2
+ Revision: 636546
- rebuild

* Wed Nov 17 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.32.1-1mdv2011.0
+ Revision: 598365
- update to new version 2.32.1

* Mon Sep 27 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.32.0-1mdv2011.0
+ Revision: 581279
- update to new version 2.32.0

* Tue Sep 14 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.92-1mdv2011.0
+ Revision: 578286
- update to new version 2.31.92

* Wed Aug 18 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.90-1mdv2011.0
+ Revision: 571215
- update to new version 2.31.90

* Wed Aug 04 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.6-1mdv2011.0
+ Revision: 565837
- update to new version 2.31.6

* Fri Jul 30 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.2-2mdv2011.0
+ Revision: 563553
- rebuild
- update to new version 2.31.2

* Sun Jul 11 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.2-1mdv2011.0
+ Revision: 550681
- update to new version 2.30.2

* Wed Mar 31 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 530228
- update to new version 2.30.0

* Mon Mar 08 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.92-1mdv2010.1
+ Revision: 516391
- new version
- drop patch
- update omf file list

* Mon Feb 22 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.91-1mdv2010.1
+ Revision: 509660
- update to new version 2.29.91

* Tue Feb 09 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.90-1mdv2010.1
+ Revision: 502987
- update to new version 2.29.90

* Wed Jan 27 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.6-1mdv2010.1
+ Revision: 497246
- update to new version 2.29.6

* Wed Jan 13 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.5-1mdv2010.1
+ Revision: 490497
- new version
- new major

* Fri Jan 08 2010 Frederic Crozat <fcrozat@mandriva.com> 2.29.4-2mdv2010.1
+ Revision: 487708
- Remove pnp.ids file, use the one from ldetect-lst now

* Tue Dec 22 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.4-1mdv2010.1
+ Revision: 481602
- update to new version 2.29.4

* Fri Dec 11 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.3-2mdv2010.1
+ Revision: 476484
- fix crash in gnome-settings-daemon without xrandr (bug #56349)

* Wed Dec 09 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.3-1mdv2010.1
+ Revision: 475428
- update to new version 2.29.3

* Thu Oct 22 2009 Frederic Crozat <fcrozat@mandriva.com> 2.28.1-1mdv2010.0
+ Revision: 458860
- Release 2.28.1

* Mon Sep 21 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446789
- update to new version 2.28.0

* Thu Sep 10 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.92-1mdv2010.0
+ Revision: 437223
- update to new version 2.27.92

* Tue Aug 25 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.91-1mdv2010.0
+ Revision: 421055
- update to new version 2.27.91

* Wed Aug 19 2009 Frederic Crozat <fcrozat@mandriva.com> 2.27.5-2mdv2010.0
+ Revision: 417962
- Remove mandriva.png from pixmaps, it is now shipped by desktop-common-data

* Tue Jul 28 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.5-1mdv2010.0
+ Revision: 402859
- new version
- update file list
- drop gnomeui dep

* Wed Jul 15 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.4-1mdv2010.0
+ Revision: 396379
- update to new version 2.27.4

* Tue Jun 16 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.3-1mdv2010.0
+ Revision: 386339
- update to new version 2.27.3

* Wed May 20 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.2-1mdv2010.0
+ Revision: 378023
- update to new version 2.26.2

* Tue Apr 14 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.1-1mdv2009.1
+ Revision: 366928
- update to new version 2.26.1

* Mon Mar 16 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 356297
- update to new version 2.26.0

* Tue Mar 03 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.92-1mdv2009.1
+ Revision: 348015
- update to new version 2.25.92

* Tue Feb 17 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.91-1mdv2009.1
+ Revision: 341222
- update to new version 2.25.91

* Wed Feb 04 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.90-1mdv2009.1
+ Revision: 337266
- update to new version 2.25.90

* Tue Jan 20 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.5-1mdv2009.1
+ Revision: 331536
- update to new version 2.25.5

* Tue Jan 06 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.4-1mdv2009.1
+ Revision: 325312
- update to new version 2.25.4

* Thu Dec 18 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.3-1mdv2009.1
+ Revision: 315826
- new version
- new major

* Tue Dec 02 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.2-1mdv2009.1
+ Revision: 309076
- update deps
- update to new version 2.25.2

* Sun Nov 09 2008 Adam Williamson <awilliamson@mandriva.org> 2.25.1.1-2mdv2009.1
+ Revision: 301224
- rebuild for new xcb

* Wed Nov 05 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.1.1-1mdv2009.1
+ Revision: 300025
- new version
- drop patch
- new major

* Wed Oct 22 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.1-2mdv2009.1
+ Revision: 296444
- rebuild for broken build system
- update to new version 2.24.1

* Tue Sep 23 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 287269
- new epiphany

* Mon Sep 08 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.92-1mdv2009.0
+ Revision: 282802
- new version

* Tue Sep 02 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.91-1mdv2009.0
+ Revision: 278809
- new version

* Tue Aug 19 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.90-1mdv2009.0
+ Revision: 273604
- new version

* Tue Aug 05 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.6-1mdv2009.0
+ Revision: 263697
- new version

* Wed Jul 23 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.5-1mdv2009.0
+ Revision: 241858
- new version

* Thu Jul 03 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.4-1mdv2009.0
+ Revision: 231019
- new version
- new version

* Mon Jun 30 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.3-1mdv2009.0
+ Revision: 230187
- new version
- update license
- update buildrequires

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue May 27 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.2-1mdv2009.0
+ Revision: 211637
- new version
- fix build

* Wed Mar 26 2008 Emmanuel Andry <eandry@mandriva.org> 2.22.0-2mdv2008.1
+ Revision: 190526
- Fix lib group

* Mon Mar 10 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 183856
- new version

* Tue Feb 26 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.92-1mdv2008.1
+ Revision: 175483
- new version

* Mon Feb 11 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.91-1mdv2008.1
+ Revision: 165444
- fix rpmlint error
- new version

* Mon Jan 28 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.90-1mdv2008.1
+ Revision: 159048
- new version

* Tue Jan 15 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.5-1mdv2008.1
+ Revision: 152168
- fix buildrequires
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Dec 18 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.4-1mdv2008.1
+ Revision: 132902
- new version
- drop patch 2

* Tue Dec 18 2007 Frederic Crozat <fcrozat@mandriva.com> 2.21.2-2mdv2008.1
+ Revision: 132449
- Patch2 (Fedora): add gnome-bg API

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.2-1mdv2008.1
+ Revision: 108622
- new version

* Mon Oct 15 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.1-1mdv2008.1
+ Revision: 98699
- new version

* Tue Sep 18 2007 Frederic Crozat <fcrozat@mandriva.com> 2.20.0-1mdv2008.0
+ Revision: 89566
- Move mo files to a new sub-package

  + GÃ¶tz Waschk <waschk@mandriva.org>
    - new version

* Wed Sep 05 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.92-1mdv2008.0
+ Revision: 79721
- new version

* Tue Aug 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.90-1mdv2008.0
+ Revision: 63283
- new version
- fix buildrequires

* Wed Aug 01 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.6-2mdv2008.0
+ Revision: 57354
- new devel name
- use scrollkeeper macros

* Mon Jul 30 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.6-1mdv2008.0
+ Revision: 56735
- fix buildrequires
- new version

* Sun Jul 08 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.5-1mdv2008.0
+ Revision: 49947
- new version

* Sun Jun 17 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.4-1mdv2008.0
+ Revision: 40612
- new version
- bump deps

* Wed Jun 06 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.3.1-1mdv2008.0
+ Revision: 36005
- new version

* Mon May 28 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.2-1mdv2008.0
+ Revision: 32121
- new version

* Wed Apr 18 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.1-1mdv2008.0
+ Revision: 14402
- new version


* Fri Mar 16 2007 Olivier Blin <oblin@mandriva.com> 2.18.0-2mdv2007.1
+ Revision: 144693
- tag lang on Gnome help files

* Tue Mar 13 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.0-1mdv2007.1
+ Revision: 142140
- new version

* Mon Feb 26 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.92-1mdv2007.1
+ Revision: 126122
- new version

* Mon Feb 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.91-1mdv2007.1
+ Revision: 120192
- new version

* Sun Jan 21 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.90-1mdv2007.1
+ Revision: 111611
- new version

* Tue Jan 09 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.5-1mdv2007.1
+ Revision: 106282
- new version

* Thu Nov 30 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.2-5mdv2007.1
+ Revision: 89202
- rebuild

* Thu Nov 30 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.2-4mdv2007.1
+ Revision: 88956
- fix buildrequires

* Wed Nov 29 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.2-3mdv2007.1
+ Revision: 88463
- rebuild

* Mon Nov 27 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.2-2mdv2007.1
+ Revision: 87661
- fix buildrequires
- new version

* Wed Nov 22 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.2-1mdv2007.1
+ Revision: 86191
- new version
- unpack patch
- Import gnome-desktop

* Fri Oct 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.1-1mdv2007.0
- New version 2.16.1

* Tue Sep 05 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.0-1mdv2007.0
- New release 2.16.0

* Wed Aug 23 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.92-1mdv2007.0
- New release 2.15.92

* Wed Aug 09 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.91-1mdv2007.0
- New release 2.15.91

* Wed Aug 02 2006 Frederic Crozat <fcrozat@mandriva.com> 2.15.90-2mdv2007.0
- Rebuild with latest dbus

* Wed Jul 26 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.90-1
- New release 2.15.90

* Tue Jul 18 2006 Frederic Crozat <fcrozat@mandriva.com> 2.15.4-2mdv2007.0
- Rebuild to drop obsolete libhowl dependency

* Wed Jul 12 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.4-1mdv2007.0
- New release 2.15.4

* Fri Jun 02 2006 Frederic Crozat <fcrozat@mandriva.com> 2.15.2-1mdv2007.0
- Release 2.15.2

* Wed May 31 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.2-1mdv2007.0
- New release 2.14.2

* Thu Apr 13 2006 Frederic Crozat <fcrozat@mandriva.com> 2.14.1.1-1mdk
- Release 2.14.1.1

* Thu Mar 02 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.3-2mdk
- Rebuild to remove howl dep

* Mon Feb 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.3-1mdk
- New release 2.12.3
- use mkrel

* Tue Nov 29 2005 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.2-1mdk
- New release 2.12.2

* Wed Oct 19 2005 Frederic Crozat <fcrozat@mandriva.com> 2.12.1-2mdk
- Fix buildrequires

* Sat Oct 08 2005 Frederic Crozat <fcrozat@mandriva.com> 2.12.1-1mdk
- Release 2.12.1

* Fri Oct 07 2005 Götz Waschk <waschk@mandriva.org> 2.12.0-3mdk
- fix buildrequires

* Fri Oct 07 2005 Götz Waschk <waschk@mandriva.org> 2.12.0-2mdk
- fix buildrequires

* Thu Oct 06 2005 Frederic Crozat <fcrozat@mandriva.com> 2.12.0-1mdk
- Release 2.12.0

* Wed Jun 29 2005 Götz Waschk <waschk@mandriva.org> 2.10.2-1mdk
- drop patch 2
- New release 2.10.2

* Sat Apr 30 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.1-5mdk 
- Patch2: fix i18n init

* Sat Apr 23 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.1-4mdk 
- Move logo to pixmaps directory

* Fri Apr 22 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.1-3mdk 
- Rename our icon file

* Fri Apr 22 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.1-2mdk 
- Fix vendor

* Thu Apr 21 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.1-1mdk 
- Release 2.10.1 (based on Götz Waschk package)
- update description with fedora one

* Tue Feb 15 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 2.8.3-1mdk 
- Release 2.8.3

* Wed Oct 20 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.8.1-1mdk
- New release 2.8.1
- Remove patch2 (merged upstream)

* Fri Jul 09 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.6.2-2mdk
- Patch2 : fix OMF validation (Mdk bug #10201)

* Wed Jun 16 2004 Götz Waschk <waschk@linux-mandrake.com> 2.6.2-1mdk
- reenable libtoolize
- New release 2.6.2

* Tue Apr 27 2004 Götz Waschk <waschk@linux-mandrake.com> 2.6.1-3mdk
- fix buildrequires

* Fri Apr 23 2004 Götz Waschk <waschk@linux-mandrake.com> 2.6.1-2mdk
- fix buildrequires

* Wed Apr 21 2004 Götz Waschk <waschk@linux-mandrake.com> 2.6.1-1mdk
- fix source location
- New release 2.6.1

* Tue Apr 06 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.6.0.1-1mdk
- Release 2.6.0.1 (with Götz help)
- add omf files and call scrollkeeper in the post script

