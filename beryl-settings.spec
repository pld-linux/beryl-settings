Summary:	A GTK+ tool to configure beryl
Summary(pl):	Narzêdzie GTK+ do konfiguracji beryla
Name:		beryl-settings
Version:        0.1.3
Release:	1
License:	GPL v2+
Group:		X11/Window Managers/Tools
Source0:	http://releases.beryl-project.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	bd88d56f32b23d42d44c85a92f0654f3
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	beryl-core-devel
BuildRequires:	dbus-glib-devel >= 0.50
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	pkgconfig
Requires:	beryl-core
Requires:	beryl-plugins
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GTK+ tool to configure beryl.

%description -l pl
Narzêdzie GTK+ do konfiguracji beryla.

%prep
%setup -q
mv -f po/{es_AR,ar}.po
mv -f po/{es_ES,es}.po
mv -f po/{fr_FR,fr}.po
mv -f po/{hu_HU,hu}.po
mv -f po/{it_IT,it}.po
mv -f po/{ja_JP,ja}.po
mv -f po/{ko_KR,ko}.po
mv -f po/{pt_PT,pt}.po
mv -f po/{sv_SE,sv}.po

    # NOTE: check the list ofter any upgrade!
cat > po/LINGUAS <<EOF
ar
es
fr
hu
it
ja
ko
pt_BR
pt
sv
zh_CN
zh_HK
zh_TW
EOF

%build
autoreconf -v --install
%{__intltoolize}
%{__glib_gettextize} --copy --force
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
    DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/beryl-settings
%{_desktopdir}/beryl-settings.desktop
%{_pixmapsdir}/*.svg
%{_mandir}/man1/*.1*
