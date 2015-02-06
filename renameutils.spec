Summary:	Set of programs designed to make renaming of multiple files faster
Name:		renameutils
Version:	0.12.0
Release:	2
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


%changelog
* Sat May 19 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.12.0-1
+ Revision: 799700
- version update 0.12.0

* Sat Apr 16 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.10.0-4
+ Revision: 653310
- rebuild

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.10.0-3mdv2010.0
+ Revision: 442677
- rebuild

* Thu Feb 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.10.0-2mdv2009.1
+ Revision: 345233
- rebuild against new readline

* Sun Sep 21 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.10.0-1mdv2009.1
+ Revision: 286397
- update to new version 0.10.0

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.9.0-4mdv2009.0
+ Revision: 260211
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.9.0-3mdv2009.0
+ Revision: 248366
- rebuild
- fix no-buildroot-tag

* Mon Dec 31 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.0-1mdv2008.1
+ Revision: 139732
- new license policy
- add missing buildrequires
- new version
- spec file clean

  + Thierry Vignaud <tv@mandriva.org>
    - BR readline-devel
    - kill re-definition of %%buildroot on Pixel's request
    - import renameutils

