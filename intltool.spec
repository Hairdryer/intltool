%include	/usr/lib/rpm/macros.perl
Summary:	Utility scripts for internationalizing various kinds of data files
Summary(pl):	Skrypty do internacjonalizacji r�znych typ�w plik�w z danymi
Name:		intltool
Version:	0.29
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/GNOME/sources/intltool/0.29/%{name}-%{version}.tar.bz2
# Source0-md5:	5d9f55dc5bd326e9da48aaa9043cf036
Patch0:		%{name}-am18.patch
URL:		http://www.gnome.org/
BuildRequires:	automake
Requires:	patch
# not detected automaticaly
Requires:	perl-XML-Parser
Provides:	xml-i18n-tools
Obsoletes:	xml-i18n-tools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Automatically extracts translatable strings from oaf, glade, bonobo
ui, nautilus theme and other files into the po files.

Automatically merges translations from po files back into .oaf files
(encoding to be 7-bit clean). I can also extend this merging mechanism
to support other types of files.

%description -l pl
Program automatycznie wyci�ga mo�liwe do przet�umaczenia ci�gi znak�w
z plik�w interfejs�w oaf, glade, bonobo, temat�w nautilusa i innych
plik�w do plik�w po.

Tak�e automatycznie w��cza t�umaczenia z plik�w po z powrotem do
plik�w oaf (koduj�c, by by�y 7-bitowe). Mechanizm ten mo�e by�
rozszerzony o inne rodzaje plik�w.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	aclocaldir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO doc/I18N-HOWTO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/intltool
%attr(755,root,root) %{_datadir}/intltool/*
%{_aclocaldir}/*.m4
%{_mandir}/man8/*.8*
