%define url_ver %(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1

%define	appver	3
%define api	3.0
%define major	17
%define libname	%mklibname %{name} %{appver} %{major}
%define girname	%mklibname %{name}-gir %{api}
%define devname	%mklibname -d %{name} %{appver}

Summary:	Package containing code shared among gnome-panel, gnome-session, nautilus, etc
Name:		gnome-desktop
Version:	3.30.2
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/GNOME
URL:		http://www.gnome.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

#BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	ldetect-lst
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xkbfile)
BuildRequires:	pkgconfig(xkeyboard-config)
BuildRequires:	pkgconfig(iso-codes)
BuildRequires:	iso-codes
BuildRequires:	pkgconfig(libseccomp)
Requires:	ldetect-lst >= 0.1.282
Conflicts:	gnome-desktop-common < 2.32.1-2
Conflicts:	%{_lib}gnome-desktop3_4 < 3.6.2-2
%rename 	gnome-desktop3

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

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:	Development libraries, include files for %{name}
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}

%description -n %{devname}
Development libraries, include files for internal library %{name}.

%prep
%setup -qn %{name}-%{version}

%build
%configure \
	--disable-static \
	--with-gnome-distributor="%{_vendor}" \
	--disable-scrollkeeper \
	--with-pnp-ids-path=%{_datadir}/misc/pnp.ids

%make LIBS='-lrt -lgmodule-2.0'

%install
%makeinstall_std
%find_lang %{name}-%{api} --with-gnome --all-name

%files -f %{name}-%{api}.lang
%doc AUTHORS COPYING ChangeLog NEWS README
%{_datadir}/gnome/gnome-version.xml
%{_libexecdir}/gnome-rr-debug

%files -n %{libname}
%{_libdir}/libgnome-desktop-%{appver}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GnomeDesktop-%{api}.typelib

%files -n %{devname}
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/GnomeDesktop-%{api}.gir

