%define		_pver	097
Summary:	tuxrip - shell script helpfull with DVD ripping 
Summary(pl):	tuxrip - skrypt pomocny przy zrzucaniu DVD
Name:		tuxrip
Version:	0.97
Release:	0.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://tuxrip.free.fr/tuxrip/%{name}%{_pver}.tar.bz2
# Source0-md5:	a30e2130917359f8b94c25bd2a8579a0
URL:		http://tuxrip.free.fr/
Requires:	libdvdcss
Requires:	libdvdread
Requires:	libogg
Requires:	libvorbis
Requires:	mplayer
Requires:	ogmtools
Requires:	perl
Requires:	transcode
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tuxrip is a Linux bash script for ripping and encoding DVD in mpeg4 
format (XviD, libavcodec). It uses a text based interface very easy 
to use and will work on most Linux distributions. The compressed 
video file can be viewed on all OS.

%description -l pl
Tuxrip to linksowy skrypt pow³oki s³u¿±cy do zrzucania oraz kodowania
DVD przy uzyciu mpeg4 (XviD, libavcodec). Wykorzystuje bardzo ³atwy 
w u¿yciu tekstowy interfejs i dzia³a na wiêkszo¶ci dystrybucji 
linuksowych. Skompresowany plik video jest niezale¿ny od systemu
operacyjnego.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install {transperl.pl,tuxrip} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%lang(en) %doc doctuxrip/en/*.{html,png}
%lang(fr) %doc doctuxrip/fr/*.{html,png}
%lang(sp) %doc doctuxrip/sp/*.{html,png}
%attr(755,root,root) %{_bindir}/*
