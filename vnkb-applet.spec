Name: vnkb-applet
Summary: A Vietnamese keyboard input for X-Window
Version: 0.0.3
Release: %mkrel 8
Group: System/Internationalization
URL: https://vinux.sourceforge.net/wikini/wakka.php?wiki=vnkb-applet
Source: http://vinux.sourceforge.net/pclouds/%{name}-%{version}.tar.bz2
Patch0: vnkb-applet-0.0.3-gnomeui-dir.patch
Patch1: vnkb-applet-0.0.3-gtk-namespace.patch
Buildroot: %{_tmppath}/%{name}-buildroot
License: GPL
Requires: locales-vi
BuildRequires: libx11-devel
BuildRequires: libglade2.0-devel
BuildRequires: gnome-panel-devel
BuildRequires: libgnomeui2-devel
BuildRequires: perl-XML-Parser
BuildRequires: gnome-common
BuildRequires: intltool

%description
Vnkb-applet is a GNOME Frontend for xvnkb
It provides both:
- a "Vietnamese Keyboard" applet in Utility,
- vnkb-docklet, which is a docklet.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
NOCONFIGURE=yes gnome-autogen.sh
export CFLAGS="%optflags -fPIC"
%configure2_5x
%make 

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root,0755)
%doc AUTHORS ChangeLog README* COPYING NEWS INSTALL
%_datadir/%name
%_datadir/gnome-2.0/ui/VnkbApplet.xml
%_libdir/vnkb-applet
%_libdir/bonobo/servers/VnkbApplet_Factory.server
%{_bindir}/vnkb-docklet


