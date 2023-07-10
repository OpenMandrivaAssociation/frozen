Name: frozen
Version: 1.1.1
Release: 1
Source0: https://github.com/serge-sans-paille/frozen/archive/refs/tags/1.1.1.tar.gz
Patch0: frozen-1.1.1-missing-include.patch
Summary: Header-only, constexpr alternative to gperf for C++14
URL: https://github.com/frozen/frozen
License: Apache-2.0
Group: Development/C and C++
BuildRequires: cmake ninja
BuildArch: noarch

%description
Header-only library that provides 0 cost initialization for immutable
containers, fixed-size containers, and various algorithms.

Frozen provides:

immutable (a.k.a. frozen), constexpr-compatible versions of std::set,
std::unordered_set, std::map and std::unordered_map.
fixed-capacity, constinit-compatible versions of std::map and
std::unordered_map with immutable, compile-time selected keys mapped to
mutable values.

0-cost initialization version of std::search for frozen needles using
Boyer-Moore or Knuth-Morris-Pratt algorithms.
The unordered_* containers are guaranteed perfect (a.k.a. no hash collision)
and the extra storage is linear with respect to the number of keys.

Once initialized, the container keys cannot be updated, and in exchange,
lookups are faster. And initialization is free when constexpr or constinit is
used.

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_includedir}/frozen
%{_datadir}/cmake/frozen
