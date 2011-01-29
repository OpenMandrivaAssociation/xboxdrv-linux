
Name:		xboxdrv-linux
License:	GPL
Group:		Emulators
URL:		http://pingus.seul.org/~grumbel/xboxdrv/
Autoreqprov:  on
Version:      0.7.0
Release:      %mkrel 1
Summary:      XBox 360 Controller Driver
Source:       %name-%version.tar.bz2
Patch0:		%name-Makefile.patch
BuildRequires: SDL-devel zlib-devel GL-devel gcc-c++ scons libusb-devel boost-devel libudev0-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Userspace Xbox/Xbox360 USB Gamepad Driver for Linux

%prep
%setup -q
%patch0 -p0

%build
%make PREFIX=/usr

%install
install -D xboxdrv %{buildroot}%{_bindir}/xboxdrv
install -D doc/xboxdrv-daemon.1 %{buildroot}%{_mandir}/man1/xboxdrv-daemon.1
install -D doc/xboxdrv.1 %{buildroot}%{_mandir}/man1/xboxdrv.1
# rm %{buildroot}/usr/local/bin/xboxdrv
# rm %{buildroot}/usr/local/man/man1/xboxdrv-daemon.1
# rm %{buildroot}/usr/local/man/man1/xboxdrv.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xboxdrv
%{_mandir}/man1/xboxdrv*

