%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api	2
%define major	17
%define libname	%mklibname %{name}-%{api}_ %{major}
%define devname	%mklibname -d %{name}-%{api}

Summary:	Package containing code shared among gnome-panel, gnome-session, nautilus, etc
Name:		gnome-desktop
Version:	2.32.1
Release:	14
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-desktop/%{url_ver}/%{name}-%{version}.tar.bz2

BuildRequires:	gtk-doc
BuildRequires:	intltool >= 0.40.0
BuildRequires:	ldetect-lst
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gnome-doc-utils)

Provides:	%{name}-%{api} = %{version}-%{release}
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

%package -n %{devname}
Summary:	Development libraries, include files for gnome-desktop
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
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
%{_libdir}/libgnome-desktop-%{api}.so.%{major}*

%files -n %{devname}
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

