#
# Conditional build
%bcond_with	postr	# flickr uploader plugin (no longer working as of 42)

Summary:	A collection of plugins for the EOG image viewer
Summary(pl.UTF-8):	Zestaw wtyczek do przeglądarki obrazków EOG
Name:		eog-plugins
Version:	44.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/eog-plugins/44/%{name}-%{version}.tar.xz
# Source0-md5:	1e2f61bd04521eb61f81727f5c5ef7be
URL:		https://wiki.gnome.org/Apps/EyeOfGnome
BuildRequires:	clutter-devel >= 1.9.4
BuildRequires:	clutter-gtk-devel >= 1.1.2
BuildRequires:	eog-devel >= 41.0
BuildRequires:	gettext-tools >= 0.19.7
BuildRequires:	glib2-devel >= 1:2.53.4
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gtk+3-devel >= 3.14.0
BuildRequires:	libchamplain-devel >= 0.12.0
BuildRequires:	libexif-devel >= 1:0.6.16
BuildRequires:	libgdata-devel >= 0.9.1
BuildRequires:	libpeas-devel >= 1.14.1
BuildRequires:	libpeas-gtk-devel >= 1.14.1
BuildRequires:	meson >= 0.58.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.53.4
Requires:	clutter >= 1.9.4
Requires:	clutter-gtk >= 1.1.2
Requires:	eog >= 41.0
Requires:	glib2 >= 1:2.53.4
Requires:	gtk+3 >= 3.14.0
Requires:	libchamplain >= 0.12.0
Requires:	libexif >= 1:0.6.16
Requires:	libgdata >= 0.9.1
Requires:	libpeas >= 1.14.1
Requires:	libpeas-gtk >= 1.14.1
Suggests:	libpeas-loader-python >= 1.14.1
%{?with_postr:Suggests:	postr}
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

%build
%meson build \
	%{?with_postr:-Dplugin_postr=true}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang eog-plugins

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f eog-plugins.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README

%{pluginsdir}/exif-display.plugin
%attr(755,root,root) %{pluginsdir}/libexif-display.so
%{_datadir}/glib-2.0/schemas/org.gnome.eog.plugins.exif-display.gschema.xml
%{_datadir}/metainfo/eog-exif-display.appdata.xml

%{pluginsdir}/export-to-folder.plugin
%{pluginsdir}/export-to-folder.py
%{_datadir}/eog/plugins/export-to-folder
%{_datadir}/glib-2.0/schemas/org.gnome.eog.plugins.export-to-folder.gschema.xml
%{_datadir}/metainfo/eog-export-to-folder.appdata.xml

%{pluginsdir}/fit-to-width.plugin
%attr(755,root,root) %{pluginsdir}/libfit-to-width.so
%{_datadir}/metainfo/eog-fit-to-width.appdata.xml

%{pluginsdir}/fullscreenbg.plugin
%{pluginsdir}/fullscreenbg.py
%{_datadir}/eog/plugins/fullscreenbg
%{_datadir}/glib-2.0/schemas/org.gnome.eog.plugins.fullscreenbg.gschema.xml
%{_datadir}/metainfo/eog-fullscreenbg.appdata.xml

%{pluginsdir}/light-theme.plugin
%attr(755,root,root) %{pluginsdir}/liblight-theme.so
%{_datadir}/metainfo/eog-light-theme.appdata.xml

%{pluginsdir}/map.plugin
%attr(755,root,root) %{pluginsdir}/libmap.so
%{_datadir}/metainfo/eog-map.appdata.xml

%{pluginsdir}/maximize-windows.plugin
%{pluginsdir}/maximize-windows.py
%{_datadir}/metainfo/eog-maximize-windows.appdata.xml

%{pluginsdir}/postasa.plugin
%attr(755,root,root) %{pluginsdir}/libpostasa.so
%{_datadir}/metainfo/eog-postasa.appdata.xml

%if %{with postr}
%{pluginsdir}/postr.plugin
%attr(755,root,root) %{pluginsdir}/libpostr.so
%{_datadir}/metainfo/eog-postr.appdata.xml
%endif

%{pluginsdir}/pythonconsole.plugin
%{pluginsdir}/pythonconsole
%{_datadir}/eog/plugins/pythonconsole
%{_datadir}/glib-2.0/schemas/org.gnome.eog.plugins.pythonconsole.gschema.xml
%{_datadir}/metainfo/eog-pythonconsole.appdata.xml

%{pluginsdir}/send-by-mail.plugin
%attr(755,root,root) %{pluginsdir}/libsend-by-mail.so
%{_datadir}/metainfo/eog-send-by-mail.appdata.xml

%{pluginsdir}/slideshowshuffle.plugin
%{pluginsdir}/slideshowshuffle.py
%{_datadir}/metainfo/eog-slideshowshuffle.appdata.xml
