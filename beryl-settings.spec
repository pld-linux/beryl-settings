Summary:	A GTK+ tool to configure beryl
Summary(pl):	Narz�dzie GTK+ do konfiguracji beryla
Name:		beryl-settings
Version:	0.1.4
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Window Managers/Tools
Source0:	http://releases.beryl-project.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	527c6cf2a91d7249b409f123602709f6
URL:		http://beryl-project.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	beryl-core-devel >= 1:0.1.3
BuildRequires:	dbus-glib-devel >= 0.50
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	pkgconfig
Requires:	beryl-core >= 1:0.1.3
Requires:	beryl-plugins >= 1:0.1.3
Obsoletes:	compiz-settings-manager
Obsoletes:	csm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GTK+ tool to configure beryl.

%description -l pl
Narz�dzie GTK+ do konfiguracji beryla.

%prep
%setup -q
mv -f po/{ca_ES,ca}.po
mv -f po/{es_ES,es}.po
mv -f po/{fr_FR,fr}.po
mv -f po/{hu_HU,hu}.po
mv -f po/{it_IT,it}.po
mv -f po/{ja_JP,ja}.po
mv -f po/{ko_KR,ko}.po
mv -f po/{pt_PT,pt}.po
mv -f po/{sv_SE,sv}.po
# sv_FI is identical to sv_SE

# NOTE: check the list after any upgrade!
cat > po/LINGUAS <<EOF
ca
es
es_AR
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
%{__intltoolize}
%{__glib_gettextize} --copy --force
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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
