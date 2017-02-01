Summary:	LinuxBand GUI front-end for MMA
Name:		linuxband
Version:	12.02.1
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://linuxband.org/assets/sources/%{name}-%{version}.tar.gz
# Source0-md5:	d87c8db9badf776fd321362b2fdb6c7a
Patch0:		grooves.patch
Patch1:		isdigit.patch
URL:		http://linuxband.org/
BuildRequires:	autoconf
BuildRequires:	glib2-devel >= 1:2.2
BuildRequires:	jack-audio-connection-kit-devel >= 0.102.0
BuildRequires:	libsmf-devel >= 1.3
Requires:	mma
Requires:	python-gtksourceview2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LinuxBand is a GUI front-end for MMA (Musical MIDI Accompaniment).
Type in the chords, choose the groove and LinuxBand will play a
musical accompaniment for you. It’s an open source alternative to
Band-in-a-Box featuring:

- Easy to use graphical interface
- Open and well-documented data format
- Output to JACK Midi to facilitate co-operation with other audio
  applications

%prep
%setup -q

%patch0 -p1
%patch1 -p1

%build
%{__autoconf}

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
%doc COPYING README.md
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/%{name}-player
%{_datadir}/%{name}
