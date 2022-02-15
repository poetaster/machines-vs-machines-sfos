# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       harbour-machines-vs-machines-sfos

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    Machines vs. Machines
Version:    1.3.2
Release:    1
Group:      Qt/Qt
License:    LICENSE
URL:        https://launchpad.net/machines-vs-machines
Source0:    %{name}-%{version}.tar.bz2
Source100:  machines-vs-machines-sfos.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  desktop-file-utils
%if "%{?vendor}" == "chum"
BuildRequires:  qt5-qttools-linguist
%endif

%description
A Game of Machine VS Machine

%if "%{?vendor}" == "chum"
PackageName: Machines vs. Machines
Type: desktop-application
Categories:
 - Game
PackagerName: Mark Washeim (poetaster)
DeveloperName: Michael Zanetti
Custom:
 - Repo: https://github.com/poetaster/machines-vs-machines-sfos
Icon: https://raw.githubusercontent.com/poetaster//machines-vs-machines-sfos/master/icons/172x172/harbour-tidings.png
Screenshots:
 - https://raw.githubusercontent.com/poetaster/machines-vs-machines-sfos/master/screen-1.png
 - https://raw.githubusercontent.com/poetaster/machines-vs-machines-sfos/master/screen-2.png
 - https://raw.githubusercontent.com/poetaster/machines-vs-machines-sfos/master/screen-3.png
Url:
  Donation: hkttps://www.paypal.me/poetasterFOSS
%endif

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
# >> files
# << files
