Summary:	A collection of plugins for the EOG image viewer
Summary(pl.UTF-8):	Zestaw wtyczek do przeglądarki obrazków EOG
Name:		eog-plugins
Version:	3.16.3
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/eog-plugins/3.16/%{name}-%{version}.tar.xz
# Source0-md5:	d116f2c181906c44d305f94624345f43
Patch0:		%{name}-configure.patch
URL:		http://live.gnome.org/EyeOfGnome/Plugins
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.11
BuildRequires:	clutter-devel >= 1.9.4
BuildRequires:	clutter-gtk-devel >= 1.1.2
BuildRequires:	eog-devel >= 3.16.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.38.0
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gtk+3-devel >= 3.14.0
BuildRequires:	intltool >= 0.50.1
BuildRequires:	libchamplain-devel >= 0.12.0
BuildRequires:	libexif-devel >= 1:0.6.16
BuildRequires:	libgdata-devel >= 0.8.0
BuildRequires:	libpeas-devel >= 1.0.0
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	pkgconfig
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.38.0
Requires:	clutter >= 1.9.4
Requires:	clutter-gtk >= 1.1.2
Requires:	eog >= 3.16.0
Requires:	glib2 >= 1:2.38.0
Requires:	gtk+3 >= 3.14.0
Requires:	libchamplain >= 0.12.0
Requires:	libexif >= 1:0.6.16
Suggests:	libpeas-gtk >= 1.0.0
Suggests:	libpeas-loader-python
Suggests:	postr
Suggests:	python-pygobject3 >= 3.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		pluginsdir	%{_libdir}/eog/plugins

%description
This package provides collection of plugins for use with the Eye of
GNOME Image Viewer.

%description -l pl.UTF-8
Ten pakiet dostarcza zestaw wtyczek do przeglądarki obrazków Eye of
GNOME (Oko GNOME).

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	POSTR=/usr/bin/postr \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{pluginsdir}/*.{la,py}
%{__rm} $RPM_BUILD_ROOT%{pluginsdir}/pythonconsole/*.py

%find_lang eog-plugins

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f eog-plugins.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/glib-2.0/schemas/org.gnome.eog.plugins.exif-display.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.eog.plugins.export-to-folder.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.eog.plugins.fullscreenbg.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.eog.plugins.pythonconsole.gschema.xml

%{_datadir}/appdata/eog-exif-display.metainfo.xml
%{_datadir}/appdata/eog-export-to-folder.metainfo.xml
%{_datadir}/appdata/eog-fit-to-width.metainfo.xml
%{_datadir}/appdata/eog-fullscreenbg.metainfo.xml
%{_datadir}/appdata/eog-hide-titlebar.metainfo.xml
%{_datadir}/appdata/eog-light-theme.metainfo.xml
%{_datadir}/appdata/eog-map.metainfo.xml
%{_datadir}/appdata/eog-maximize-windows.metainfo.xml
%{_datadir}/appdata/eog-postasa.metainfo.xml
%{_datadir}/appdata/eog-postr.metainfo.xml
%{_datadir}/appdata/eog-pythonconsole.metainfo.xml
%{_datadir}/appdata/eog-send-by-mail.metainfo.xml
%{_datadir}/appdata/eog-slideshowshuffle.metainfo.xml

%dir %{pluginsdir}/__pycache__

%attr(755,root,root) %{pluginsdir}/libexif-display.so
%{pluginsdir}/exif-display.plugin

%attr(755,root,root) %{pluginsdir}/libfit-to-width.so
%{pluginsdir}/fit-to-width.plugin

%dir %{_datadir}/eog/plugins/fullscreenbg
%{pluginsdir}/fullscreenbg.plugin
%{pluginsdir}/__pycache__/fullscreenbg*.pyc
%{_datadir}/eog/plugins/fullscreenbg/preferences_dialog.ui

%attr(755,root,root) %{pluginsdir}/libmap.so
%{pluginsdir}/map.plugin

%attr(755,root,root) %{pluginsdir}/libpostr.so
%{pluginsdir}/postr.plugin

%attr(755,root,root) %{pluginsdir}/libpostasa.so
%{pluginsdir}/postasa.plugin

%{pluginsdir}/maximize-windows.plugin
%{pluginsdir}/__pycache__/maximize-windows*.pyc

%{pluginsdir}/pythonconsole
%{pluginsdir}/pythonconsole.plugin
%dir %{_datadir}/eog/plugins/pythonconsole
%{_datadir}/eog/plugins/pythonconsole/config.ui

%attr(755,root,root) %{pluginsdir}/libsend-by-mail.so
%{pluginsdir}/send-by-mail.plugin

%{pluginsdir}/slideshowshuffle.plugin
%{pluginsdir}/__pycache__/slideshowshuffle*.pyc

%dir %{_datadir}/eog/plugins/export-to-folder
%{pluginsdir}/export-to-folder.plugin
%{pluginsdir}/__pycache__/export-to-folder*.pyc
%{_datadir}/eog/plugins/export-to-folder/preferences_dialog.ui

%attr(755,root,root) %{pluginsdir}/libhide-titlebar.so
%{pluginsdir}/hide-titlebar.plugin

%attr(755,root,root) %{pluginsdir}/liblight-theme.so
%{pluginsdir}/light-theme.plugin
