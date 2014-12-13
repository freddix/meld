Summary:	Visual diff and merge tool
Name:		meld
Version:	3.12.2
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://ftp.gnome.org/pub/gnome/sources/meld/3.12/%{name}-%{version}.tar.xz
# Source0-md5:	a11c4abf923d136e410fa9e8217c0bba
URL:		https://wiki.gnome.org/Apps/Meld
BuildRequires:	gettext-devel
BuildRequires:	itstool
BuildRequires:	libxml2-progs
BuildArch:	noarch
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	glib-gio-gsettings
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	shared-mime-info
Requires:	gsettings-desktop-schemas
Requires:	gtksourceview3
Requires:	python-pygobject3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Meld is a GNOME visual diff and merge tool. It integrates especially
well with CVS. The diff viewer lets you edit files in place (diffs
update dynamically), and a middle column shows detailed changes and
allows merges. The margins show location of changes for easy
navigation, and it also features a tabbed interface that allows you to
open many diffs at once.

%prep
%setup -q

%{__sed} -i 's|.py|.pyc|g' meld/vc/__init__.py

# broken
rm po/{hu,ja,ru}.po

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py \
	--no-compile-schemas	\
	--no-update-icon-cache	\
	install			\
	--optimize=2		\
	--root=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_mime_database
%update_gsettings_cache

%postun
%update_icon_cache hicolor
%update_mime_database
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/meld
%{py_sitescriptdir}/meld
%{_datadir}/meld
%{_datadir}/glib-2.0/schemas/org.gnome.meld.gschema.xml
%{_datadir}/mime/packages/meld.xml
%{_desktopdir}/meld.desktop
%{_iconsdir}/hicolor/*/actions/*.*
%{_iconsdir}/hicolor/*/apps/*.*
%{_mandir}/man1/meld.1*

