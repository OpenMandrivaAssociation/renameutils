Summary:	Set of programs designed to make renaming of multiple files faster
Name:		renameutils
Version:	0.12.0
Release:	1
Group:		File tools
License:	GPLv2+
URL:		http://www.nongnu.org/renameutils/
Source0:	http://savannah.nongnu.org/download/renameutils/%{name}-%{version}.tar.gz
BuildRequires:	readline-devel
BuildRequires:	termcap-devel
Patch0:		renameutils-0.12.0-typo.patch
Patch1:		renameutils-0.12-type2.patch

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
%patch0 -p1
%patch1 -p1

%build
%configure2_5x \
	--disable-rpath

%make

%install
%makeinstall_std

%find_lang %{name} --all-name

%files -f %{name}.lang
%doc README AUTHORS ChangeLog NEWS TODO
%{_bindir}/*
%{_mandir}/man1/*
