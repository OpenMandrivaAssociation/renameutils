Summary:	Set of programs designed to make renaming of multiple files faster
Name:		renameutils
Version:	0.10.0
Release:	%mkrel 1
Group:		File tools
License:	GPLv2+
URL:		http://www.nongnu.org/renameutils/
Source:		http://savannah.nongnu.org/download/renameutils/%{name}-%{version}.tar.bz2
BuildRequires:	libreadline-devel
BuildRequires:	libtermcap-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%setup -q

%build
%configure2_5x \
	--disable-rpath

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README AUTHORS ChangeLog NEWS TODO
%{_bindir}/*
%{_mandir}/man1/*
