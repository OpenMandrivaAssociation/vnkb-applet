Name: vnkb-applet
Summary: A Vietnamese keyboard input for X-Window
Version: 0.0.3
Release: %mkrel 8
Group: System/Internationalization
URL: http://vinux.sourceforge.net/wikini/wakka.php?wiki=vnkb-applet
Source: http://vinux.sourceforge.net/pclouds/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot
License: GPL
Requires: locales-vi
BuildRequires:	X11-devel gtk+2-devel libglade2.0-devel
BuildRequires:	gnomeui2-devel gnome-panel-devel
BuildRequires:  perl-XML-Parser

%description
Vnkb-applet is a GNOME Frontend for xvnkb
It provides both:
- a "Vietnamese Keyboard" applet in Utility,
- vnkb-docklet, which is a docklet.

%prep
%setup -q

%build
#configure --with-unikey-gtk (default: excluded)
CFLAGS="$RPM_OPT_FLAGS -fPIC" %configure 
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


