Name:           gzip
Version:        1.9
Release:        16
Summary:        A data compression utility

License:        GPLv3+ and GFDL
URL:            https://www.gnu.org/software/gzip
Source0:        https://ftp.gnu.org/gnu/gzip/gzip-%{version}.tar.xz
Source1:        colorzgrep.csh
Source2:        colorzgrep.sh

Patch0:         gnulib.patch
Patch1:         gzip-fix-use-of-uninitialized-memory.patch
Patch2:         gzexe.patch
Patch9000:      fix-verbose-disable.patch

BuildRequires:  gcc texinfo
Requires:       coreutils
Conflicts:      filesystem < 3
Provides:       /bin/gunzip
Provides:       /bin/gzip
Provides:       /bin/zcat
Provides:       bundled(gnulib)

%description
gzip is a single-file/stream lossless data compression
utility, where the resulting compressed file generally
has the suffix .gz.

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure
%make_build

%install
rm -rf %RPM_BUILD_ROOT
%make_install
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/profile.d
install -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/profile.d
# ncompress provides uncompress, may cause conflict.
rm -f %{buildroot}%{_bindir}/uncompress

%check
make check

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/*
%{_sysconfdir}/profile.d/*
%exclude %{_infodir}/dir

%files help
%doc NEWS TODO THANKS
%{_infodir}/*info*
%{_mandir}/man1/*

%changelog
* Mon Sep 30 2019 shenyangyang<shenyangyang4@huawei.com> - 1.9-16
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:fix the conflict of infodir/dir with libtasn1

* Tue Sep 24 2019 shenyangyang<shenyangyang4@huawei.com> - 1.9-15
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:revise help package

* Fri Aug 16 2019 openEuler Builteam <buildteam@openeuler.org> - 1.9-14
- Rewrite spec file

* Fri Aug 09 2019 fangyufa<fangyufa1@huawei.com> - 1.9-13
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify info of patch

* Thu Aug 08 2019 fangyufa<fangyufa1@huawei.com> - 1.9-12
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify of patch

* Wed Jul 31 2019 zhuguodong<zhuguodong7@huawei.com> - 1.9-11
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: openEuler Debranding

* Fri Jun 14 2019 cangyi<cangyi@huawei.com> - 1.9-10
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix gzexe unable to (auto)decompress

* Fri Mar 15 2019 zhangyujing <zhangyujing1@huawei.com> - 1.9-9
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:gzip fix use of uninitialized memory

* Fri Jan 25 2019 Yeqing Peng<pengyeqing@huawei.com> - 1.9-8
- Type:enhancement
- ID:NA
- SUG:restart
- DESC:fix verbose disable

* Thu Jul 26 2018 zhuguodong<zhuguodong7@huawei.com> - 1.9-7
- package init

