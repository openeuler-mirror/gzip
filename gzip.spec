Name:           gzip
Version:        1.10
Release:        3
Summary:        A data compression utility

License:        GPLv3+
URL:            https://www.gnu.org/software/gzip
Source0:        https://ftp.gnu.org/gnu/gzip/gzip-%{version}.tar.xz

Patch0:         gzexe.patch
Patch9000:      fix-verbose-disable.patch
Patch9100:      performance-neoncrc32-and-prfm.patch

Patch6000:      backport-0001-CVE-2022-1271.patch
Patch6001:      backport-0002-CVE-2022-1271.patch
Patch6002:      backport-0003-CVE-2022-1271.patch

BuildRequires:  gcc texinfo automake autoconf
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
%ifarch aarch64
export CFLAGS="${CFLAGS:-%optflags} -march=armv8-a+crc"
%endif
autoreconf
%configure
%make_build

%install
rm -rf %RPM_BUILD_ROOT
%make_install
# ncompress provides uncompress, may cause conflict.
rm -f %{buildroot}%{_bindir}/uncompress

%check
make check

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/*
%exclude %{_infodir}/dir

%files help
%doc NEWS TODO THANKS
%{_infodir}/*info*
%{_mandir}/man1/*

%changelog
* Wed Apr 20 2022 shixuantong <shixuantong@h-partners.com> - 1.10-3
- fix CVE-2022-1271

* Thu Apr 14 2022 renhongxun <renhongxun@h-partners.com> - 1.10-2
- update license from GPLv3+,GFDL to GPLv3+

* Fri Apr 24 2020 BruceGW <gyl93216@163.com> - 1.10-1
- update upstream to 1.10

* Fri Jan 17 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.9-18
- Type:performance improve
- ID:NA
- SUG:NA
- DESC:delete useless scripts for grep

* Mon Nov 11 2019 liqiang<liqiang64@huawei.com> - 1.9-17
- Type:performance improve
- ID:NA
- SUG:NA
- DESC:use neon crc32 api and PRFM instruction to improve performance.

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

