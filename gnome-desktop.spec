%define	api_version 2
%define lib_major   2
%define lib_name	%mklibname %{name}-%{api_version}_ %{lib_major}

%define req_libgnomeui_version 2.1.0
%define req_startup_notification_version 0.5

Summary:          Package containing code shared among gnome-panel, gnome-session, nautilus, etc
Name:             gnome-desktop
Version: 2.19.6
Release: %mkrel 1
License:          GPL/LGPL
Group:            Graphical desktop/GNOME
Source0:          http://ftp.gnome.org/pub/GNOME/sources/gnome-desktop/%{name}-%{version}.tar.bz2
# (fc) 2.2.0.1-2mdk search in KDE 3.1 icon path
Patch1:		  gnome-desktop-2.3.7-crystalsvg.patch
BuildRoot:        %{_tmppath}/%{name}-%{version}-root
URL:              http://www.gnome.org
Requires:	  libgnomeui2 >= %{req_libgnomeui_version}
BuildRequires:    libgnomeui2-devel >= %{req_libgnomeui_version}
BuildRequires:	  startup-notification-devel >= %{req_startup_notification_version}
BuildRequires: gtk+2-devel >= 2.11.3
BuildRequires:	  scrollkeeper
BuildRequires:	gnome-doc-utils >= 0.3.2
BuildRequires:	libxslt-proc
BuildRequires:    perl-XML-Parser

%description
This package contains some data files and other shared components of the
GNOME user environment.

%package -n %{lib_name}
Summary:	%{summary}
Group:		%{group}
Requires:   %{name} >= %{version}
Provides:	%{name}-%{api_version} = %{version}-%{release}
Requires: libstartup-notification-1 >= %{req_startup_notification_version}

%description -n %{lib_name}
This package contains an internal library
(libgnomedesktop) used to implement some portions of the GNOME
desktop.

%package -n %{lib_name}-devel
Summary:	Static libraries, include files for gnome-desktop
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-%{api_version}-devel = %{version}-%{release}
Requires:	%{lib_name} = %{version}
Requires:   libgnomeui2-devel
Requires:   libstartup-notification-1-devel >= %{req_startup_notification_version}

%description -n %{lib_name}-devel
Static libraries, include files for internal library libgnomedesktop.

%prep
%setup -q
%patch1 -p1 -b .crystalsvg

%build

%configure2_5x --with-gnome-distributor="%vendor" --disable-scrollkeeper

%make


%install
rm -rf $RPM_BUILD_ROOT %{name}-2.0.lang

GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std 

%find_lang %{name}-2.0
for omf in %buildroot%_datadir/omf/*/{*-??.omf,*-??_??.omf};do
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name-2.0.lang
done
for d in `ls -1 %buildroot%_datadir/gnome/help/`; do
  %find_lang $d --with-gnome
  cat $d.lang >> %name-2.0.lang
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
ln -s %{_liconsdir}/mandrake.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/mandriva.png

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%post
if [ -x %{_bindir}/scrollkeeper-update ]; then %{_bindir}/scrollkeeper-update -q || true ; fi

%postun
if [ -x %{_bindir}/scrollkeeper-update ]; then %{_bindir}/scrollkeeper-update -q || true ; fi

%post -p /sbin/ldconfig -n %{lib_name}

%postun -p /sbin/ldconfig -n %{lib_name}

%files -f %{name}-2.0.lang
%defattr (-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/*
%{_mandir}/man1/*
%dir %{_datadir}/omf/*
%{_datadir}/omf/*/*-C.omf
%{_datadir}/gnome-about
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%files -n %{lib_name}
%defattr (-, root, root)
%{_libdir}/*.so.*

%files -n %{lib_name}-devel
%defattr (-, root, root)
%{_includedir}/*
%{_libdir}/*.a
%attr(644,root,root) %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%_datadir/gtk-doc/html/*
