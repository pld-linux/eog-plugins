Summary:	A collection of plugins for the EOG image viewer
Summary(pl.UTF-8):	Zestaw wtyczek do przeglądarki obrazków EOG
Name:		eog-plugins
Version:	3.1.3
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/eog-plugins/3.1/%{name}-%{version}.tar.xz
# Source0-md5:	95bcba1d7573fd833c77672a186008c4
Patch0:		%{name}-configure.patch
URL:		http://live.gnome.org/EyeOfGnome/Plugins
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	clutter-gtk-devel >= 0.10.0
BuildRequires:	eog-devel >= 3.0.0
BuildRequires:	gettext-devel
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libchamplain-devel >= 0.12.0
BuildRequires:	libexif-devel >= 0.6.16
BuildRequires:	libgdata-devel >= 0.8.0
BuildRequires:	libpeas-devel >= 1.0.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	eog >= 3.0.0
Suggests:	postr
Suggests:	python-pygobject >= 2.28.0
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
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{pluginsdir}/*.{la,py}

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

%attr(755,root,root) %{pluginsdir}/libexif-display.so
%{pluginsdir}/exif-display.plugin
%{_datadir}/eog/plugins/exif-display

%attr(755,root,root) %{pluginsdir}/libfit-to-width.so
%{pluginsdir}/fit-to-width.plugin

%attr(755,root,root) %{pluginsdir}/libmap.so
%{pluginsdir}/map.plugin

%attr(755,root,root) %{pluginsdir}/libpostr.so
%{pluginsdir}/postr.plugin

%attr(755,root,root) %{pluginsdir}/libpostasa.so
%{pluginsdir}/postasa.plugin
%{_datadir}/eog/plugins/postasa

%dir %{pluginsdir}/pythonconsole
%{pluginsdir}/pythonconsole/*.py*
%{pluginsdir}/pythonconsole.plugin

%attr(755,root,root) %{pluginsdir}/libsend-by-mail.so
%{pluginsdir}/send-by-mail.plugin

%{pluginsdir}/slideshowshuffle.py[co]
%{pluginsdir}/slideshowshuffle.plugin
