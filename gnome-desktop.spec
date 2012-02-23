%define	api_version 2
%define lib_major   17
%define libname	%mklibname %{name}-%{api_version}_ %{lib_major}
%define develname %mklibname -d %{name}-%{api_version}

Summary:	Package containing code shared among gnome-panel, gnome-session, nautilus, etc
Name:		gnome-desktop
Version:	2.32.1
Release:	7
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/GNOME
URL:		http://www.gnome.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-desktop/%{name}-%{version}.tar.bz2

BuildRequires: startup-notification-devel >= 0.5
BuildRequires: gtk+2-devel >= 2.14.0
BuildRequires: glib2-devel >= 2.19.1
BuildRequires: libGConf2-devel
BuildRequires: gtk-doc
BuildRequires: gnome-doc-utils >= 0.3.2
BuildRequires: libxslt-proc
BuildRequires: intltool >= 0.40.0
BuildRequires: ldetect-lst

Provides:	%{name}-%{api_version} = %{version}-%{release}
Requires: ldetect-lst >= 0.1.282
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
Obsoletes: %mklibname -d %{name}-2_ 2

%description -n %{develname}
Development libraries, include files for internal library libgnomedesktop.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static \
	--with-gnome-distributor="%vendor" \
	--disable-scrollkeeper \
	--with-pnp-ids-path=%{_datadir}/misc/pnp.ids

%make LIBS=-lm

%install
rm -rf %{buildroot}

GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std 
%find_lang %{name}-2.0
find %{buildroot} -name '*.la' -delete

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

