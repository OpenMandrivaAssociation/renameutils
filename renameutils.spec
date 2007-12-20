%define name renameutils
%define version 0.8.1
%define release %mkrel 1

Name: %{name}
Summary: Set of programs designed to make renaming of multiple files faster
Version: %{version}
Release: %{release}
Source: http://savannah.nongnu.org/download/renameutils/%{name}-%{version}.tar.bz2
Group: File tools
URL: http://www.nongnu.org/renameutils/
License: GPL
BuildRequires: readline-devel

%description
The file renaming utilities (renameutils for short) are a set of programs 
designed to make renaming of multiple files faster and less cumbersome. 
It currently consists of two programs: "qmv" and "imv". qmv allows files 
to be renamed by editing their names in any text editor. Since the files 
are listed after each other, this allows common changes to be made more 
quickly. imv ("interactive mv") is trivial but useful when you are too 
lazy to type (or even complete) the name of the file to rename. It 
allows the filename to be edited in the terminal using the GNU readline 
library. This is also useful when renaming files in Midnight Commander, 
where the whole filename has to be entered again.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
%configure

%make

%install
%makeinstall

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT 

%files -f %name.lang
%defattr(-,root,root)
%doc COPYING README ABOUT-NLS AUTHORS ChangeLog INSTALL NEWS TODO
%_bindir/*
%_mandir/man1/*

